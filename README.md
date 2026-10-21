# Drupal 7 API archive

An offline archive of the Drupal 7 core API reference: the material on
api.drupal.org/api/drupal/7.x, rebuilt from the **Drupal 7.103** source code.
7.103 is the final Drupal 7 release. Drupal 7 reached end of life on
January 5, 2025.

It's written in plain markdown, so it reads well on GitHub and is fast for
LLMs to search.

**Start at [`api/INDEX.md`](api/INDEX.md).**

## What's here

| Path | What it is |
|---|---|
| `api/` | Generated reference: 10,221 pages covering 4,729 functions, 364 hooks, 766 classes and interfaces, 4,047 methods, 280 constants and 67 topics |
| `api/symbols.tsv` | Lookup table for every symbol, with its page and a summary |
| `source/` | The unmodified Drupal 7.103 core source |
| `tools/` | The extractor (PHP tokenizer) and renderer that build `api/` |

Docblocks and code are copied verbatim from the source. Anything computed,
such as summaries, indexes and hook implementation lists, is labelled as
derived. See `api/INDEX.md` for the exact rules.

## Rebuilding

```sh
tools/build.sh          # defaults to 7.103
tools/build.sh 7.103    # or name another 7.x tag
```

This needs `git`, `php` (8.x) and `python3`. The script clones core from
github.com/drupal/drupal, replaces `source/` and `api/`, and regenerates
everything.

## License

- `source/` and `api/` come from Drupal core, which is
  **GPL-2.0-or-later**. See [`LICENSE`](LICENSE) and
  [`COPYRIGHT.txt`](COPYRIGHT.txt).
- The build tools in `tools/` are original work under the **MIT** license.
  See [`LICENSE-MIT`](LICENSE-MIT).

Drupal is a registered trademark of Dries Buytaert. This archive is not
affiliated with or endorsed by the Drupal Association.
