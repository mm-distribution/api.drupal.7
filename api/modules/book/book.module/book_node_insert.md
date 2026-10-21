# book_node_insert()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 937–947 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L937-L947)
- **Module/theme:** book
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function book_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function book_node_insert($node) {
  if (!empty($node->book['bid'])) {
    if ($node->book['bid'] == 'new') {
      // New nodes that are their own book.
      $node->book['bid'] = $node->nid;
    }
    $node->book['nid'] = $node->nid;
    $node->book['menu_name'] = book_menu_name($node->book['bid']);
    _book_update_outline($node);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
