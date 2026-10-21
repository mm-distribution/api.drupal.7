# modules/book/book-all-books-block.tpl.php

- **Source:** [local](../../../../source/modules/book/book-all-books-block.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book-all-books-block.tpl.php) · 24 lines
- **Module/theme:** book

## File documentation

```text
@file
Default theme implementation for rendering book outlines within a block.

This template is used only when the block is configured to "show block on all
pages", which presents multiple independent books on all pages.

Available variables:
- $book_menus: Array of book outlines keyed to the parent book ID. Call
  render() on each to print it as an unordered list.

@see template_preprocess_book_all_books_block()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
