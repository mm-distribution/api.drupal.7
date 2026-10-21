# actions_do()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 58–143 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L58-L143)
- **Topics:** [actions](../../topics/actions.md)

## Signature

```php
function actions_do($action_ids, $object = NULL, $context = NULL, $a1 = NULL, $a2 = NULL)
```

## Documentation

```text
Performs a given list of actions by executing their callback functions.

Given the IDs of actions to perform, this function finds out what the
callback functions for the actions are by querying the database. Then
it calls each callback using the function call $function($object, $context,
$a1, $a2), passing the input arguments of this function (see below) to the
action function.

@param $action_ids
  The IDs of the actions to perform. Can be a single action ID or an array
  of IDs. IDs of configurable actions must be given as numeric action IDs;
  IDs of non-configurable actions may be given as action function names.
@param $object
  The object that the action will act on: a node, user, or comment object.
@param $context
  Associative array containing extra information about what triggered
  the action call, with $context['hook'] giving the name of the hook
  that resulted in this call to actions_do().
@param $a1
  Passed along to the callback.
@param $a2
  Passed along to the callback.

@return
  An associative array containing the results of the functions that
  perform the actions, keyed on action ID.

@ingroup actions
```

## Code

```php
function actions_do($action_ids, $object = NULL, $context = NULL, $a1 = NULL, $a2 = NULL) {
  // $stack tracks the number of recursive calls.
  static $stack;
  $stack++;
  if ($stack > variable_get('actions_max_stack', 35)) {
    watchdog('actions', 'Stack overflow: too many calls to actions_do(). Aborting to prevent infinite recursion.', array(), WATCHDOG_ERROR);
    return;
  }
  $actions = array();
  $available_actions = actions_list();
  $actions_result = array();
  if (is_array($action_ids)) {
    $conditions = array();
    foreach ($action_ids as $action_id) {
      if (is_numeric($action_id)) {
        $conditions[] = $action_id;
      }
      elseif (isset($available_actions[$action_id])) {
        $actions[$action_id] = $available_actions[$action_id];
      }
    }

    // When we have action instances we must go to the database to retrieve
    // instance data.
    if (!empty($conditions)) {
      $query = db_select('actions');
      $query->addField('actions', 'aid');
      $query->addField('actions', 'type');
      $query->addField('actions', 'callback');
      $query->addField('actions', 'parameters');
      $query->condition('aid', $conditions, 'IN');
      $result = $query->execute();
      foreach ($result as $action) {
        $actions[$action->aid] = $action->parameters ? unserialize($action->parameters) : array();
        $actions[$action->aid]['callback'] = $action->callback;
        $actions[$action->aid]['type'] = $action->type;
      }
    }

    // Fire actions, in no particular order.
    foreach ($actions as $action_id => $params) {
      // Configurable actions need parameters.
      if (is_numeric($action_id)) {
        $function = $params['callback'];
        if (function_exists($function)) {
          $context = array_merge($context, $params);
          $actions_result[$action_id] = $function($object, $context, $a1, $a2);
        }
        else {
          $actions_result[$action_id] = FALSE;
        }
      }
      // Singleton action; $action_id is the function name.
      else {
        $actions_result[$action_id] = $action_id($object, $context, $a1, $a2);
      }
    }
  }
  // Optimized execution of a single action.
  else {
    // If it's a configurable action, retrieve stored parameters.
    if (is_numeric($action_ids)) {
      $action = db_query("SELECT callback, parameters FROM {actions} WHERE aid = :aid", array(':aid' => $action_ids))->fetchObject();
      $function = $action->callback;
      if (function_exists($function)) {
        $context = array_merge($context, unserialize($action->parameters));
        $actions_result[$action_ids] = $function($object, $context, $a1, $a2);
      }
      else {
        $actions_result[$action_ids] = FALSE;
      }
    }
    // Singleton action; $action_ids is the function name.
    else {
      if (function_exists($action_ids)) {
        $actions_result[$action_ids] = $action_ids($object, $context, $a1, $a2);
      }
      else {
        // Set to avoid undefined index error messages later.
        $actions_result[$action_ids] = FALSE;
      }
    }
  }
  $stack--;
  return $actions_result;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
