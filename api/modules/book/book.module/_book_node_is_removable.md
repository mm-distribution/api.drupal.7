# _book_node_is_removable()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 228–230 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L228-L230)
- **Module/theme:** book

## Signature

```php
function _book_node_is_removable($node)
```

## Documentation

```text
Determines if a node can be removed from the book.

A node can be removed from a book if it is actually in a book and it either
is not a top-level page or is a top-level page with no children.

@param $node
  The node to remove from the outline.
```

## Code

```php
function _book_node_is_removable($node) {
  return (!empty($node->book['bid']) && (($node->book['bid'] != $node->nid) || !$node->book['has_children']));
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
