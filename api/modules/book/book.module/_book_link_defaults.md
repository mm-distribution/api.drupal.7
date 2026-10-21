# _book_link_defaults()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1060–1062 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1060-L1062)
- **Module/theme:** book

## Signature

```php
function _book_link_defaults($nid)
```

## Documentation

```text
Returns an array with default values for a book page's menu link.

@param $nid
  The ID of the node whose menu link is being created.

@return
  The default values for the menu link.
```

## Code

```php
function _book_link_defaults($nid) {
  return array('original_bid' => 0, 'menu_name' => '', 'nid' => $nid, 'bid' => 0, 'router_path' => 'node/%', 'plid' => 0, 'mlid' => 0, 'has_children' => 0, 'weight' => 0, 'module' => 'book', 'options' => array());
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
