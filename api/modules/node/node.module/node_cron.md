# node_cron()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 158–162 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L158-L162)
- **Module/theme:** node
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function node_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function node_cron() {
  db_delete('history')
    ->condition('timestamp', NODE_NEW_LIMIT, '<')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
