# _book_toc_recurse()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1168–1182 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1168-L1182)
- **Module/theme:** book

## Signature

```php
function _book_toc_recurse($tree, $indent, &$toc, $exclude, $depth_limit)
```

## Documentation

```text
Recursively processes and formats menu items for book_toc().

This helper function recursively modifies the table of contents array for
each item in the menu tree, ignoring items in the exclude array or at a depth
greater than the limit. Truncates titles over thirty characters and appends
an indentation string incremented by depth.

@param $tree
  The data structure of the book's menu tree. Includes hidden links.
@param $indent
  A string appended to each menu item title. Increments by '--' per depth
  level.
@param $toc
  Reference to the table of contents array. This is modified in place, so the
  function does not have a return value.
@param $exclude
  (optional) An array of menu link ID values. Any link whose menu link ID is
  in this array will be excluded (along with its children). Defaults to an
  empty array.
@param $depth_limit
  Any link deeper than this value will be excluded (along with its children).
```

## Code

```php
function _book_toc_recurse($tree, $indent, &$toc, $exclude, $depth_limit) {
  foreach ($tree as $data) {
    if ($data['link']['depth'] > $depth_limit) {
      // Don't iterate through any links on this level.
      break;
    }

    if (!in_array($data['link']['mlid'], $exclude)) {
      $toc[$data['link']['mlid']] = $indent . ' ' . truncate_utf8($data['link']['title'], 30, TRUE, TRUE);
      if ($data['below']) {
        _book_toc_recurse($data['below'], $indent . '--', $toc, $exclude, $depth_limit);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
