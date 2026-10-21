# Drupal 7 API archive — start here

Reference documentation for **Drupal 7.103** core (the final Drupal 7
release), generated from the source code. It is the same material as
api.drupal.org/api/drupal/7.x, built directly from the core source.

## How to find things

- **Know the name?** Look it up in [`symbols.tsv`](symbols.tsv): one line per
  function, method, class, constant and property, with its page and a one-line
  summary. Grep for `^name\t`.
- **Implementing a hook?** See [`hooks.md`](hooks.md). It lists all 364 core
  hooks and 11 callbacks, each with how many core modules implement it. Every
  hook page lists those implementations.
- **Learning a subsystem?** See [`topics.md`](topics.md). These are the core
  `@defgroup` topics (Database abstraction layer, Form builder, Menu system,
  Hooks, and others), each with its full documentation and member list.
- **Browsing by file?** See [`files.md`](files.md). Every source file has an
  `_file.md` page with its `@file` docs, constants and an item list.
- **Classes:** [`classes.md`](classes.md). **Constants:** [`constants.md`](constants.md).

## Page layout

Pages mirror the source tree: `api/<source path>/<name>.md`. For example:

- `api/modules/node/node.module/node_load.md` is a function.
- `api/includes/database/select.inc/SelectQuery.md` is a class.
- `api/includes/database/select.inc/SelectQuery/fields.md` is a method.
- `api/includes/bootstrap.inc/_file.md` is a file page, which also documents
  that file's constants.

Each function page has **Signature**, **Documentation** (the docblock) and
**Code** (the full function). A few lines at the top give its file, line
numbers, module, topics, and the hook it implements.

## What is exact and what is derived

- **Exact:** docblocks and code are copied verbatim from source. For docblocks,
  only the comment syntax is removed: `/**`, `*/`, and the leading ` * ` on
  each line. Doxygen tags (`@param`, `@return`, `@code`, `@see`, `@ingroup`,
  and so on) are left as written.
- **Derived:** summaries, member lists, hook implementation lists and every
  index file are computed by `tools/render.py`. They are labelled "derived".
- **Full source:** the complete, unmodified core tree is in `../source/`.
