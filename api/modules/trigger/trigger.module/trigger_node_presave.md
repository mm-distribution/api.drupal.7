# trigger_node_presave()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 326–328 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L326-L328)
- **Module/theme:** trigger
- **Implements:** [hook_node_presave()](../../node/node.api.php/hook_node_presave.md)

## Signature

```php
function trigger_node_presave($node)
```

## Documentation

```text
Implements hook_node_presave().
```

## Code

```php
function trigger_node_presave($node) {
  _trigger_node($node, 'node_presave');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
