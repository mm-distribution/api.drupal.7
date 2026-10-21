# modules/book/book-export-html.tpl.php

- **Source:** [local](../../../../source/modules/book/book-export-html.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book-export-html.tpl.php) · 53 lines
- **Module/theme:** book

## File documentation

```text
@file
Default theme implementation for printed version of book outline.

Available variables:
- $title: Top level node title.
- $head: Header tags.
- $language: Language code. e.g. "en" for english.
- $language_rtl: TRUE or FALSE depending on right to left language scripts.
- $base_url: URL to home page.
- $contents: Nodes within the current outline rendered through
  book-node-export-html.tpl.php.

@see template_preprocess_book_export_html()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
