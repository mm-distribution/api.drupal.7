# trigger_get_assigned_actions()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 188–196 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L188-L196)
- **Module/theme:** trigger

## Signature

```php
function trigger_get_assigned_actions($hook)
```

## Documentation

```text
Gets the action IDs of actions to be executed for a hook.

@param $hook
  The name of the hook being fired.

@return
  An array whose keys are action IDs that the user has associated with
  this trigger, and whose values are arrays containing the action type and
  label.
```

## Code

```php
function trigger_get_assigned_actions($hook) {
  $actions = &drupal_static(__FUNCTION__, array());
  if (!isset($actions[$hook])) {
    $actions[$hook] = db_query("SELECT ta.aid, a.type, a.label FROM {trigger_assignments} ta LEFT JOIN {actions} a ON ta.aid = a.aid WHERE ta.hook = :hook ORDER BY ta.weight", array(
      ':hook' => $hook,
    ))->fetchAllAssoc('aid', PDO::FETCH_ASSOC);
  }
  return $actions[$hook];
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
