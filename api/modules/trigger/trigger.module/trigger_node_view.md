# trigger_node_view()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 312–314 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L312-L314)
- **Module/theme:** trigger
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function trigger_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function trigger_node_view($node, $view_mode) {
  _trigger_node($node, 'node_view', $view_mode);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
