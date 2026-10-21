# trigger_actions_delete()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 627–632 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L627-L632)
- **Module/theme:** trigger
- **Implements:** [hook_actions_delete()](../../system/system.api.php/hook_actions_delete.md)

## Signature

```php
function trigger_actions_delete($aid)
```

## Documentation

```text
Implements hook_actions_delete().

Removes all trigger entries for the given action, when an action is deleted.
```

## Code

```php
function trigger_actions_delete($aid) {
  db_delete('trigger_assignments')
    ->condition('aid', $aid)
    ->execute();
  drupal_static_reset('trigger_get_assigned_actions');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
