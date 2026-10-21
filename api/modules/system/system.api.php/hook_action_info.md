# hook_action_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4021–4044 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4021-L4044)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [actions](../../../topics/actions.md)

## Signature

```php
function hook_action_info()
```

## Documentation

```text
Declares information about actions.

Any module can define actions, and then call actions_do() to make those
actions happen in response to events. The trigger module provides a user
interface for associating actions with module-defined triggers, and it makes
sure the core triggers fire off actions when their events happen.

An action consists of two or three parts:
- an action definition (returned by this hook)
- a function which performs the action (which by convention is named
  MODULE_description-of-function_action)
- an optional form definition function that defines a configuration form
  (which has the name of the action function with '_form' appended to it.)

The action function takes two to four arguments, which come from the input
arguments to actions_do().

@return
  An associative array of action descriptions. The keys of the array
  are the names of the action functions, and each corresponding value
  is an associative array with the following key-value pairs:
  - 'type': The type of object this action acts upon. Core actions have types
    'node', 'user', 'comment', and 'system'.
  - 'label': The human-readable name of the action, which should be passed
    through the t() function for translation.
  - 'configurable': If FALSE, then the action doesn't require any extra
    configuration. If TRUE, then your module must define a form function with
    the same name as the action function with '_form' appended (e.g., the
    form for 'node_assign_owner_action' is 'node_assign_owner_action_form'.)
    This function takes $context as its only parameter, and is paired with
    the usual _submit function, and possibly a _validate function.
  - 'triggers': An array of the events (that is, hooks) that can trigger this
    action. For example: array('node_insert', 'user_update'). You can also
    declare support for any trigger by returning array('any') for this value.
  - 'behavior': (optional) A machine-readable array of behaviors of this
    action, used to signal additionally required actions that may need to be
    triggered. Currently recognized behaviors by Trigger module:
    - 'changes_property': If an action with this behavior is assigned to a
      trigger other than a "presave" hook, any save actions also assigned to
      this trigger are moved later in the list. If no save action is present,
      one will be added.
      Modules that are processing actions (like Trigger module) should take
      special care for the "presave" hook, in which case a dependent "save"
      action should NOT be invoked.

@ingroup actions
```

## Code

```php
function hook_action_info() {
  return array(
    'comment_unpublish_action' => array(
      'type' => 'comment',
      'label' => t('Unpublish comment'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('comment_presave', 'comment_insert', 'comment_update'),
    ),
    'comment_unpublish_by_keyword_action' => array(
      'type' => 'comment',
      'label' => t('Unpublish comment containing keyword(s)'),
      'configurable' => TRUE,
      'behavior' => array('changes_property'),
      'triggers' => array('comment_presave', 'comment_insert', 'comment_update'),
    ),
    'comment_save_action' => array(
      'type' => 'comment',
      'label' => t('Save comment'),
      'configurable' => FALSE,
      'triggers' => array('comment_insert', 'comment_update'),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_action_info()".

- [actions_loop_test_action_info()](../../simpletest/tests/actions_loop_test.module/actions_loop_test_action_info.md) — `modules/simpletest/tests/actions_loop_test.module`
- [comment_action_info()](../../comment/comment.module/comment_action_info.md) — `modules/comment/comment.module`
- [node_action_info()](../../node/node.module/node_action_info.md) — `modules/node/node.module`
- [system_action_info()](../system.module/system_action_info.md) — `modules/system/system.module`
- [trigger_test_action_info()](../../trigger/tests/trigger_test.module/trigger_test_action_info.md) — `modules/trigger/tests/trigger_test.module`
- [user_action_info()](../../user/user.module/user_action_info.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
