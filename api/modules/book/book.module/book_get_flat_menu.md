# book_get_flat_menu()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 721–732 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L721-L732)
- **Module/theme:** book

## Signature

```php
function book_get_flat_menu($book_link)
```

## Documentation

```text
Gets the book menu tree for a page and returns it as a linear array.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  A linear array of menu links in the order that the links are shown in the
  menu, so the previous and next pages are the elements before and after the
  element corresponding to the current node. The children of the current node
  (if any) will come immediately after it in the array, and links will only
  be fetched as deep as one level deeper than $book_link.
```

## Code

```php
function book_get_flat_menu($book_link) {
  $flat = &drupal_static(__FUNCTION__, array());

  if (!isset($flat[$book_link['mlid']])) {
    // Call menu_tree_all_data() to take advantage of the menu system's caching.
    $tree = menu_tree_all_data($book_link['menu_name'], $book_link, $book_link['depth'] + 1);
    $flat[$book_link['mlid']] = array();
    _book_flatten_menu($tree, $flat[$book_link['mlid']]);
  }

  return $flat[$book_link['mlid']];
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
