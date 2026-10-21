# trigger_node_delete()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 340–342 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L340-L342)
- **Module/theme:** trigger
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function trigger_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function trigger_node_delete($node) {
  _trigger_node($node, 'node_delete');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
