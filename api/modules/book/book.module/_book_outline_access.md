# _book_outline_access()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 203–205 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L203-L205)
- **Module/theme:** book

## Signature

```php
function _book_outline_access($node)
```

## Documentation

```text
Access callback: Determines if the outline tab is accessible.

@param $node
  The node whose outline tab is to be viewed.
```

## Code

```php
function _book_outline_access($node) {
  return user_access('administer book outlines') && node_access('view', $node);
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
