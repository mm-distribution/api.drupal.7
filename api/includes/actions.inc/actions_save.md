# actions_save()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 343–362 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L343-L362)

## Signature

```php
function actions_save($function, $type, $params, $label, $aid = NULL)
```

## Documentation

```text
Saves an action and its user-supplied parameter values to the database.

@param $function
  The name of the function to be called when this action is performed.
@param $type
  The type of action, to describe grouping and/or context, e.g., 'node',
  'user', 'comment', or 'system'.
@param $params
  An associative array with parameter names as keys and parameter values as
  values.
@param $label
  A user-supplied label of this particular action, e.g., 'Send e-mail
  to Jim'.
@param $aid
  The ID of this action. If omitted, a new action is created.

@return
  The ID of the action.
```

## Code

```php
function actions_save($function, $type, $params, $label, $aid = NULL) {
  // aid is the callback for singleton actions so we need to keep a separate
  // table for numeric aids.
  if (!$aid) {
    $aid = db_next_id();
  }

  db_merge('actions')
    ->key(array('aid' => $aid))
    ->fields(array(
      'callback' => $function,
      'type' => $type,
      'parameters' => serialize($params),
      'label' => $label,
    ))
    ->execute();

  watchdog('actions', 'Action %action saved.', array('%action' => $label));
  return $aid;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
