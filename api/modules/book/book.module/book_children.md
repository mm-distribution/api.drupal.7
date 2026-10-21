# book_children()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 832–856 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L832-L856)
- **Module/theme:** book

## Signature

```php
function book_children($book_link)
```

## Documentation

```text
Formats the menu links for the child pages of the current page.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  HTML for the links to the child pages of the current page.
```

## Code

```php
function book_children($book_link) {
  $flat = book_get_flat_menu($book_link);

  $children = array();

  if ($book_link['has_children']) {
    // Walk through the array until we find the current page.
    do {
      $link = array_shift($flat);
    }
    while ($link && ($link['mlid'] != $book_link['mlid']));
    // Continue though the array and collect the links whose parent is this page.
    while (($link = array_shift($flat)) && $link['plid'] == $book_link['mlid']) {
      $data['link'] = $link;
      $data['below'] = '';
      $children[] = $data;
    }
  }

  if ($children) {
    $elements = menu_tree_output($children);
    return drupal_render($elements);
  }
  return '';
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
