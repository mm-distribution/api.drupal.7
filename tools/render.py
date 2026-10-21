#!/usr/bin/env python3
"""Render extracted Drupal 7 API items (from extract.php) into markdown.

Usage: render.py <items.json> <drupal-root> <out-dir> <version>

Exactness rules:
- Docblocks: only the comment syntax is removed (the opening slash-star-star,
  the closing star-slash, and each line's leading whitespace plus one "*" and
  one following space). Everything else is kept byte for byte.
- Code: whole source lines, copied exactly.
- Anything computed (summaries, hook implementation lists, indexes) lives in
  sections or files clearly labelled as derived.
"""
import json
import os
import re
import sys
from collections import defaultdict

items_path, root, out, version = sys.argv[1:5]
data = json.load(open(items_path, encoding="utf-8"))
GH = f"https://github.com/drupal/drupal/blob/{version}"
API = "https://api.drupal.org/api/drupal"


def read_lines(path, _cache={}):
    if path not in _cache:
        with open(os.path.join(root, path), encoding="utf-8", errors="surrogateescape") as f:
            _cache[path] = f.read().split("\n")
    return _cache[path]


def clean_doc(doc):
    """Strip comment syntax only."""
    if not doc:
        return ""
    s = doc
    s = re.sub(r"^\s*/\*\*", "", s, count=1)
    s = re.sub(r"\*/\s*$", "", s, count=1)
    raw = s.split("\n")
    # Column where text starts on normal " * text" lines; used for the rare
    # line that lacks its "*", so its relative indentation is kept exactly.
    widths = [len(m.group(1)) + 2 for m in (re.match(r"^([ \t]*)\* ", l) for l in raw) if m]
    col = max(set(widths), key=widths.count) if widths else 0
    out_lines = []
    for line in raw:
        m = re.match(r"^[ \t]*\*(?: ?)(.*)$", line)
        if m:
            out_lines.append(m.group(1))
        elif not line.strip():
            out_lines.append("")
        else:
            lead = len(line) - len(line.lstrip(" \t"))
            out_lines.append(line[min(lead, col):] if widths else line.strip())
    while out_lines and not out_lines[0].strip():
        out_lines.pop(0)
    while out_lines and not out_lines[-1].strip():
        out_lines.pop()
    return "\n".join(out_lines)


def summary(doc):
    """Derived one-liner: first paragraph before any @tag, whitespace collapsed."""
    text = clean_doc(doc)
    para = []
    for line in text.split("\n"):
        if not line.strip() or line.lstrip().startswith("@"):
            if para:
                break
            if line.lstrip().startswith("@file"):
                continue
            if line.lstrip().startswith("@"):
                break
            continue
        para.append(line.strip())
    return " ".join(para)


def fence(text, lang=""):
    longest = max((len(m) for m in re.findall(r"`{3,}", text)), default=0)
    f = "`" * max(3, longest + 1)
    return f"{f}{lang}\n{text}\n{f}"


def code_lines(item):
    lines = read_lines(item["file"])
    return "\n".join(lines[item["line"] - 1:item["end_line"]])


def module_of(path, _cache={}):
    """Nearest directory containing a .info file names the module/theme."""
    d = os.path.dirname(path)
    key = d
    if key in _cache:
        return _cache[key]
    while d:
        full = os.path.join(root, d)
        infos = [f for f in os.listdir(full) if f.endswith(".info")]
        if infos:
            base = os.path.basename(d)
            name = base if f"{base}.info" in infos else infos[0][:-5]
            _cache[key] = name
            return name
        d = os.path.dirname(d)
    _cache[key] = None
    return None


# ---------------------------------------------------------------- page paths
items = data["items"]
files = {f["path"]: f for f in data["files"]}
groups = {g["name"]: g for g in data["groups"]}
taken = defaultdict(set)


def safe(name):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name.lstrip("$"))


for it in items:
    base = f"api/{it['file']}"
    if it["type"] in ("function", "class", "interface", "trait"):
        stem = safe(it["name"])
        while stem.lower() in taken[base]:
            stem += "_"
        taken[base].add(stem.lower())
        it["page"] = f"{base}/{stem}.md"
    elif it["type"] == "method":
        it["page"] = f"{base}/{safe(it['class'])}/{safe(it['name'])}.md"
    elif it["type"] in ("property", "class_constant"):
        it["page"] = f"{base}/{safe(it['class'])}.md"
    else:  # constant: documented on the file page
        it["page"] = f"{base}/_file.md"
    it["clean"] = clean_doc(it["doc"])
    it["summary"] = summary(it["doc"])
    it["module"] = module_of(it["file"])


def rel(from_page, to_page, anchor=""):
    r = os.path.relpath(to_page, os.path.dirname(from_page))
    return r + (f"#{anchor}" if anchor else "")


def anchor(name):
    return re.sub(r"[^a-z0-9_-]", "", name.lower().replace(" ", "-"))


# ------------------------------------------------------- group memberships
members = defaultdict(list)
for it in items:
    gs = list(it["groups"])
    gs += re.findall(r"@ingroup\s+(\S+)", it["clean"])
    seen = []
    for g in gs:
        if g not in seen:
            seen.append(g)
    it["all_groups"] = seen
    for g in seen:
        members[g].append(it)

# ----------------------------------------------------- hook implementations
hooks = {it["name"]: it for it in items
         if it["type"] == "function" and it["file"].endswith(".api.php") and it["name"].startswith("hook_")}
impls = defaultdict(list)
for it in items:
    if it["type"] != "function":
        continue
    for h in re.findall(r"Implements?\s+(hook_[A-Za-z0-9_]+)\(\)", it["clean"]):
        impls[h].append(it)
        it.setdefault("implements", []).append(h)

by_class = defaultdict(list)
for it in items:
    if it.get("class"):
        by_class[(it["file"], it["class"])].append(it)

pages = defaultdict(list)  # page -> list of chunks


def meta_block(it, page):
    kind = {"function": "Function", "method": "Method", "class": "Class", "interface": "Interface",
            "trait": "Trait", "constant": "Constant", "class_constant": "Class constant",
            "property": "Property"}[it["type"]]
    if it["file"].endswith(".api.php") and it["name"].startswith("hook_") and it["type"] == "function":
        kind = "Hook (documentation function)"
    src_local = rel(page, f"source/{it['file']}")
    ln = f"L{it['line']}" + (f"-L{it['end_line']}" if it["end_line"] != it["line"] else "")
    lines = [
        f"- **Type:** {kind}",
        f"- **File:** [`{it['file']}`]({rel(page, f'api/{it['file']}/_file.md')}), lines {it['line']}–{it['end_line']}"
        f" · [local source]({src_local}) · [GitHub]({GH}/{it['file']}#{ln})",
    ]
    if it.get("class"):
        cls = next((c for c in items if c["type"] in ("class", "interface", "trait")
                    and c["name"] == it["class"] and c["file"] == it["file"]), None)
        if cls:
            lines.append(f"- **Class:** [{it['class']}]({rel(page, cls['page'])})")
    if it["module"]:
        lines.append(f"- **Module/theme:** {it['module']}")
    if it["all_groups"]:
        gl = []
        for g in it["all_groups"]:
            gl.append(f"[{g}]({rel(page, f'api/topics/{safe(g)}.md')})" if g in groups else g)
        lines.append("- **Topics:** " + ", ".join(gl))
    for h in it.get("implements", []):
        if h in hooks:
            lines.append(f"- **Implements:** [{h}()]({rel(page, hooks[h]['page'])})")
    return "\n".join(lines)


def item_body(it, page, level=2):
    h = "#" * level
    parts = []
    parts.append(f"{h} Signature\n\n" + fence(it["signature"], "php"))
    if it["clean"]:
        parts.append(f"{h} Documentation\n\n" + fence(it["clean"], "text"))
    else:
        parts.append(f"{h} Documentation\n\n_No docblock in source._")
    if it["type"] in ("function", "method"):
        parts.append(f"{h} Code\n\n" + fence(code_lines(it), "php"))
    return "\n\n".join(parts)


# ----------------------------------------------------------- function pages
for it in items:
    if it["type"] not in ("function", "method"):
        continue
    page = it["page"]
    title = f"{it['class']}::{it['name']}()" if it["type"] == "method" else f"{it['name']}()"
    chunks = [f"# {title}", meta_block(it, page), item_body(it, page)]
    if it["name"] in hooks and hooks[it["name"]] is it:
        im = sorted(impls.get(it["name"], []), key=lambda x: (x["module"] or "", x["name"]))
        lst = "\n".join(f"- [{x['name']}()]({rel(page, x['page'])}) — `{x['file']}`" for x in im) or "_None found._"
        chunks.append("## Implementations in Drupal core (derived)\n\n"
                      "Functions whose docblock says \"Implements " + it["name"] + "()\".\n\n" + lst)
    chunks.append(f"---\n_Drupal {version} · [{it['file']}]({GH}/{it['file']}) · "
                  "Licensed GPL-2.0-or-later (see LICENSE)._")
    pages[page] = chunks

# -------------------------------------------------------------- class pages
for it in items:
    if it["type"] not in ("class", "interface", "trait"):
        continue
    page = it["page"]
    chunks = [f"# {it['name']}", meta_block(it, page), item_body(it, page)]
    mem = by_class[(it["file"], it["name"])]
    consts = [m for m in mem if m["type"] == "class_constant"]
    props = [m for m in mem if m["type"] == "property"]
    meths = [m for m in mem if m["type"] == "method"]
    if consts:
        chunks.append("## Constants\n\n" + "\n\n".join(
            f"### {m['name']}\n\n" + fence(m["signature"], "php") + (("\n\n" + fence(m["clean"], "text")) if m["clean"] else "")
            for m in consts))
    if props:
        chunks.append("## Properties\n\n" + "\n\n".join(
            f"### {m['name']}\n\n" + fence(m["signature"], "php") + (("\n\n" + fence(m["clean"], "text")) if m["clean"] else "")
            for m in props))
    if meths:
        chunks.append("## Methods (derived index)\n\n" + "\n".join(
            f"- [{m['name']}()]({rel(page, m['page'])})" + (f" — {m['summary']}" if m["summary"] else "")
            for m in meths))
    chunks.append(f"---\n_Drupal {version} · [{it['file']}]({GH}/{it['file']}) · "
                  "Licensed GPL-2.0-or-later (see LICENSE)._")
    pages[page] = chunks

# --------------------------------------------------------------- file pages
by_file = defaultdict(list)
for it in items:
    by_file[it["file"]].append(it)

for path, f in files.items():
    page = f"api/{path}/_file.md"
    chunks = [f"# {path}"]
    meta = [f"- **Source:** [local]({rel(page, f'source/{path}')}) · [GitHub]({GH}/{path}) · {f['lines']} lines"]
    mod = module_of(path)
    if mod:
        meta.append(f"- **Module/theme:** {mod}")
    chunks.append("\n".join(meta))
    if f["doc"]:
        chunks.append("## File documentation\n\n" + fence(clean_doc(f["doc"]), "text"))
    its = by_file[path]
    for label, types in (("Functions", ("function",)), ("Classes and interfaces", ("class", "interface", "trait"))):
        sel = [i for i in its if i["type"] in types]
        if sel:
            chunks.append(f"## {label} (derived index)\n\n" + "\n".join(
                f"- [{i['name']}{'()' if i['type'] == 'function' else ''}]({rel(page, i['page'])})"
                + (f" — {i['summary']}" if i["summary"] else "") for i in sel))
    consts = [i for i in its if i["type"] == "constant"]
    if consts:
        chunks.append("## Constants\n\n" + "\n\n".join(
            f"### {c['name']}\n\n- Line {c['line']}" + (
                "; topics: " + ", ".join(c["all_groups"]) if c["all_groups"] else "")
            + "\n\n" + fence(c["signature"], "php") + (("\n\n" + fence(c["clean"], "text")) if c["clean"] else "")
            for c in consts))
    chunks.append(f"---\n_Drupal {version} · Licensed GPL-2.0-or-later (see LICENSE)._")
    pages[page] = chunks

# -------------------------------------------------------------- topic pages
order = {"function": 0, "constant": 1, "class": 2, "interface": 2, "trait": 2, "method": 3,
         "property": 4, "class_constant": 4}
for name, g in groups.items():
    page = f"api/topics/{safe(name)}.md"
    chunks = [f"# {g['title'] or name}", f"- **Topic id:** `{name}`\n"
              f"- **Defined in:** [`{g['file']}`]({rel(page, f'api/{g['file']}/_file.md')}), line {g['line']}"
              f" · [GitHub]({GH}/{g['file']}#L{g['line']})"]
    chunks.append("## Documentation\n\n" + fence(clean_doc(g["doc"]), "text"))
    mem = sorted(members.get(name, []), key=lambda i: (order[i["type"]], i.get("class") or "", i["name"]))
    if mem:
        lst = []
        for i in mem:
            label = f"{i['class']}::{i['name']}" if i.get("class") else i["name"]
            if i["type"] in ("function", "method"):
                label += "()"
            lst.append(f"- [{label}]({rel(page, i['page'], anchor(i['name']) if i['type'] == 'constant' else '')})"
                       f" ({i['type'].replace('_', ' ')})" + (f" — {i['summary']}" if i["summary"] else ""))
        chunks.append(f"## Members (derived, {len(mem)})\n\nFrom `@ingroup` tags and `@addtogroup`/`@defgroup` "
                      "`@{ … @}` regions in the source.\n\n" + "\n".join(lst))
    chunks.append(f"---\n_Drupal {version} · Licensed GPL-2.0-or-later (see LICENSE)._")
    pages[page] = chunks

# ------------------------------------------------------------------ indexes
idx = "api/hooks.md"
pages[idx] = ["# Hooks (derived index)",
              f"All {len(hooks)} hooks documented in Drupal {version} core `*.api.php` files, with the number of "
              "core implementations.",
              "\n".join(f"- [{h}()]({rel(idx, hooks[h]['page'])}) — {hooks[h]['summary']} "
                        f"_({len(impls.get(h, []))} impl.)_" for h in sorted(hooks))]
callbacks = sorted((i for i in items if i["type"] == "function" and i["file"].endswith(".api.php")
                    and not i["name"].startswith("hook_")), key=lambda i: i["name"])
if callbacks:
    pages[idx] += ["## Callbacks", "Documentation functions for callbacks, from the same `*.api.php` files.",
                   "\n".join(f"- [{c['name']}()]({rel(idx, c['page'])}) — {c['summary']}" for c in callbacks)]

idx = "api/topics.md"
pages[idx] = ["# Topics (derived index)",
              "Topic groups defined with `@defgroup` in core.",
              "\n".join(f"- [{groups[n]['title'] or n}]({rel(idx, f'api/topics/{safe(n)}.md')}) — `{n}`, "
                        f"{len(members.get(n, []))} members" for n in sorted(groups, key=lambda n: (groups[n]['title'] or n).lower()))]

idx = "api/classes.md"
cls = sorted((i for i in items if i["type"] in ("class", "interface", "trait")), key=lambda i: i["name"].lower())
pages[idx] = ["# Classes and interfaces (derived index)",
              "\n".join(f"- [{i['name']}]({rel(idx, i['page'])}) ({i['type']}) — `{i['file']}`"
                        + (f" — {i['summary']}" if i["summary"] else "") for i in cls)]

idx = "api/constants.md"
cs = sorted((i for i in items if i["type"] == "constant"), key=lambda i: i["name"])
pages[idx] = ["# Constants (derived index)",
              "\n".join(f"- [{i['name']}]({rel(idx, i['page'], anchor(i['name']))}) — `{i['file']}`"
                        + (f" — {i['summary']}" if i["summary"] else "") for i in cs)]


def tree_lines():
    out_l = []
    for path in sorted(files):
        f = files[path]
        s = summary(f["doc"]) if f["doc"] else ""
        out_l.append(f"- [{path}]({rel('api/files.md', f'api/{path}/_file.md')})" + (f" — {s}" if s else ""))
    return "\n".join(out_l)


pages["api/files.md"] = ["# Files (derived index)", f"All {len(files)} PHP source files in Drupal {version} core.",
                         tree_lines()]

# ------------------------------------------------------------- write pages
for page, chunks in pages.items():
    full = os.path.join(out, page)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", errors="surrogateescape") as fh:
        fh.write("\n\n".join(chunks).rstrip() + "\n")

# Symbol table for fast lookup (grep-friendly).
with open(os.path.join(out, "api/symbols.tsv"), "w", encoding="utf-8") as fh:
    fh.write("name\ttype\tclass\tfile\tline\tpage\tsummary\n")
    for it in sorted(items, key=lambda i: (i["name"].lower(), i["file"])):
        anc = f"#{anchor(it['name'])}" if it["type"] in ("constant", "property", "class_constant") else ""
        fh.write("\t".join([it["name"], it["type"], it.get("class") or "", it["file"], str(it["line"]),
                            it["page"] + anc, it["summary"].replace("\t", " ")]) + "\n")

stats = {
    "files": len(files), "functions": sum(1 for i in items if i["type"] == "function"),
    "hooks": len(hooks), "classes": len(cls), "methods": sum(1 for i in items if i["type"] == "method"),
    "constants": len(cs), "topics": len(groups), "pages": len(pages),
}
json.dump(stats, open(os.path.join(out, "api/.stats.json"), "w"), indent=1)
print(json.dumps(stats))
