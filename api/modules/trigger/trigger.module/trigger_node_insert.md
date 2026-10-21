# trigger_node_insert()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 333–335 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L333-L335)
- **Module/theme:** trigger
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function trigger_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function trigger_node_insert($node) {
  _trigger_node($node, 'node_insert');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
