# book_prev()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 765–797 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L765-L797)
- **Module/theme:** book

## Signature

```php
function book_prev($book_link)
```

## Documentation

```text
Fetches the menu link for the previous page of the book.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  A fully loaded menu link for the page before the one represented in
  $book_link.
```

## Code

```php
function book_prev($book_link) {
  // If the parent is zero, we are at the start of a book.
  if ($book_link['plid'] == 0) {
    return NULL;
  }
  $flat = book_get_flat_menu($book_link);
  reset($flat);
  $curr = NULL;
  do {
    $prev = $curr;
    $curr = current($flat);
    $key = key($flat);
    next($flat);
  } while ($key && $key != $book_link['mlid']);

  if ($key == $book_link['mlid']) {
    // The previous page in the book may be a child of the previous visible link.
    if ($prev['depth'] == $book_link['depth'] && $prev['has_children']) {
      // The subtree will have only one link at the top level - get its data.
      $tree = book_menu_subtree_data($prev);
      $data = array_shift($tree);
      // The link of interest is the last child - iterate to find the deepest one.
      while ($data['below']) {
        $data = end($data['below']);
      }

      return $data['link'];
    }
    else {
      return $prev;
    }
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
