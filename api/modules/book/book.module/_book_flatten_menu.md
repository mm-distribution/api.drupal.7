# _book_flatten_menu()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 744–753 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L744-L753)
- **Module/theme:** book

## Signature

```php
function _book_flatten_menu($tree, &$flat)
```

## Documentation

```text
Recursively converts a tree of menu links to a flat array.

@param $tree
  A tree of menu links in an array.
@param $flat
  A flat array of the menu links from $tree, passed by reference.

@see book_get_flat_menu().
```

## Code

```php
function _book_flatten_menu($tree, &$flat) {
  foreach ($tree as $data) {
    if (!$data['link']['hidden']) {
      $flat[$data['link']['mlid']] = $data['link'];
      if ($data['below']) {
        _book_flatten_menu($data['below'], $flat);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
