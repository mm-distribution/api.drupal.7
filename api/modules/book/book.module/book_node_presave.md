# book_node_presave()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 919–932 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L919-L932)
- **Module/theme:** book
- **Implements:** [hook_node_presave()](../../node/node.api.php/hook_node_presave.md)

## Signature

```php
function book_node_presave($node)
```

## Documentation

```text
Implements hook_node_presave().
```

## Code

```php
function book_node_presave($node) {
  // Always save a revision for non-administrators.
  if (!empty($node->book['bid']) && !user_access('administer nodes')) {
    $node->revision = 1;
    // The database schema requires a log message for every revision.
    if (!isset($node->log)) {
      $node->log = '';
    }
  }
  // Make sure a new node gets a new menu link.
  if (empty($node->nid)) {
    $node->book['mlid'] = NULL;
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
