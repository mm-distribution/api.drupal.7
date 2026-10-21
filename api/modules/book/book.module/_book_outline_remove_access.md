# _book_outline_remove_access()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 215–217 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L215-L217)
- **Module/theme:** book

## Signature

```php
function _book_outline_remove_access($node)
```

## Documentation

```text
Access callback: Determines if the user can remove nodes from the outline.

@param $node
  The node to remove from the outline.

@see book_menu()
```

## Code

```php
function _book_outline_remove_access($node) {
  return _book_node_is_removable($node) && _book_outline_access($node);
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
