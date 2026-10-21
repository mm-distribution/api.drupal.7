# trigger_node_update()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 319–321 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L319-L321)
- **Module/theme:** trigger
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function trigger_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function trigger_node_update($node) {
  _trigger_node($node, 'node_update');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
