# actions_synchronize()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 274–321 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L274-L321)

## Signature

```php
function actions_synchronize($delete_orphans = FALSE)
```

## Documentation

```text
Synchronizes actions that are provided by modules in hook_action_info().

Actions provided by modules in hook_action_info() implementations are
synchronized with actions that are stored in the actions database table.
This is necessary so that actions that do not require configuration can
receive action IDs.

@param $delete_orphans
  If TRUE, any actions that exist in the database but are no longer
  found in the code (for example, because the module that provides them has
  been disabled) will be deleted.
```

## Code

```php
function actions_synchronize($delete_orphans = FALSE) {
  $actions_in_code = actions_list(TRUE);
  $actions_in_db = db_query("SELECT aid, callback, label FROM {actions} WHERE parameters = ''")->fetchAllAssoc('callback', PDO::FETCH_ASSOC);

  // Go through all the actions provided by modules.
  foreach ($actions_in_code as $callback => $array) {
    // Ignore configurable actions since their instances get put in when the
    // user adds the action.
    if (!$array['configurable']) {
      // If we already have an action ID for this action, no need to assign aid.
      if (isset($actions_in_db[$callback])) {
        unset($actions_in_db[$callback]);
      }
      else {
        // This is a new singleton that we don't have an aid for; assign one.
        db_insert('actions')
          ->fields(array(
            'aid' => $callback,
            'type' => $array['type'],
            'callback' => $callback,
            'parameters' => '',
            'label' => $array['label'],
            ))
          ->execute();
        watchdog('actions', "Action '%action' added.", array('%action' => $array['label']));
      }
    }
  }

  // Any actions that we have left in $actions_in_db are orphaned.
  if ($actions_in_db) {
    $orphaned = array_keys($actions_in_db);

    if ($delete_orphans) {
      $actions = db_query('SELECT aid, label FROM {actions} WHERE callback IN (:orphaned)', array(':orphaned' => $orphaned))->fetchAll();
      foreach ($actions as $action) {
        actions_delete($action->aid);
        watchdog('actions', "Removed orphaned action '%action' from database.", array('%action' => $action->label));
      }
    }
    else {
      $link = l(t('Remove orphaned actions'), 'admin/config/system/actions/orphan');
      $count = count($actions_in_db);
      $orphans = implode(', ', $orphaned);
      watchdog('actions', '@count orphaned actions (%orphans) exist in the actions table. !link', array('@count' => $count, '%orphans' => $orphans, '!link' => $link), WATCHDOG_INFO);
    }
  }
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
