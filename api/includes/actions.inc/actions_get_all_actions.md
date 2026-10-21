# actions_get_all_actions()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 190–198 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L190-L198)

## Signature

```php
function actions_get_all_actions()
```

## Documentation

```text
Retrieves all action instances from the database.

This function differs from the actions_list() function, which gathers
actions by invoking hook_action_info(). The actions returned by this
function and the actions returned by actions_list() are partially
synchronized. Non-configurable actions from hook_action_info()
implementations are put into the database when actions_synchronize() is
called, which happens when admin/config/system/actions is visited.
Configurable actions are not added to the database until they are configured
in the user interface, in which case a database row is created for each
configuration of each action.

@return
  Associative array keyed by numeric action ID. Each value is an associative
  array with keys 'callback', 'label', 'type' and 'configurable'.
```

## Code

```php
function actions_get_all_actions() {
  $actions = db_query("SELECT aid, type, callback, parameters, label FROM {actions}")->fetchAllAssoc('aid', PDO::FETCH_ASSOC);
  foreach ($actions as &$action) {
    $action['configurable'] = (bool) $action['parameters'];
    unset($action['parameters']);
    unset($action['aid']);
  }
  return $actions;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
