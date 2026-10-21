# _book_parent_depth_limit()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1029–1031 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1029-L1031)
- **Module/theme:** book

## Signature

```php
function _book_parent_depth_limit($book_link)
```

## Documentation

```text
Finds the depth limit for items in the parent select.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  The depth limit for items in the parent select.
```

## Code

```php
function _book_parent_depth_limit($book_link) {
  return MENU_MAX_DEPTH - 1 - (($book_link['mlid'] && $book_link['has_children']) ? menu_link_children_relative_depth($book_link) : 0);
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
