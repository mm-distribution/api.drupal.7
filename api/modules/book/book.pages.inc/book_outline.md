# book_outline()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 115–118 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L115-L118)
- **Module/theme:** book

## Signature

```php
function book_outline($node)
```

## Documentation

```text
Menu callback: Shows the outline form for a single node.

@param $node
  The book node for which to show the outline.

@return string
  A HTML-formatted string with the outline form for a single node.

@see book_menu()
```

## Code

```php
function book_outline($node) {
  drupal_set_title($node->title);
  return drupal_get_form('book_outline_form', $node);
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
