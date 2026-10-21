# book_node_update()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 952–962 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L952-L962)
- **Module/theme:** book
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function book_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function book_node_update($node) {
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
