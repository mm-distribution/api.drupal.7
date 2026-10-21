# book_toc()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1199–1205 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1199-L1205)
- **Module/theme:** book

## Signature

```php
function book_toc($bid, $depth_limit, $exclude = array())
```

## Documentation

```text
Returns an array of book pages in table of contents order.

@param $bid
  The ID of the book whose pages are to be listed.
@param $depth_limit
  Any link deeper than this value will be excluded (along with its children).
@param $exclude
  Optional array of menu link ID values. Any link whose menu link ID is in
  this array will be excluded (along with its children).

@return
  An array of (menu link ID, title) pairs for use as options for selecting a
  book page.
```

## Code

```php
function book_toc($bid, $depth_limit, $exclude = array()) {
  $tree = menu_tree_all_data(book_menu_name($bid));
  $toc = array();
  _book_toc_recurse($tree, '', $toc, $exclude, $depth_limit);

  return $toc;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
