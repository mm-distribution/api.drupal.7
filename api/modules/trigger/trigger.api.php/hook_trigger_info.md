# hook_trigger_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/trigger/trigger.api.php`](_file.md), lines 42–62 · [local source](../../../../source/modules/trigger/trigger.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.api.php#L42-L62)
- **Module/theme:** trigger
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_trigger_info()
```

## Documentation

```text
Declare triggers (events) for users to assign actions to.

This hook is used by the trigger module to create a list of triggers (events)
that users can assign actions to. Your module is responsible for detecting
that the events have occurred, calling trigger_get_assigned_actions() to find
out which actions the user has associated with your trigger, and then calling
actions_do() to fire off the actions.

@return
  A nested associative array.
  - The outermost key is the name of the module that is defining the triggers.
    This will be used to create a local task (tab) in the trigger module's
    user interface. A contrib module may supply a trigger for a core module by
    giving the core module's name as the key. For example, you could use the
    'node' key to add a node-related trigger.
    - Within each module, each individual trigger is keyed by a hook name
      describing the particular trigger (this is not visible to the user, but
      can be used by your module for identification).
      - Each trigger is described by an associative array. Currently, the only
        key-value pair is 'label', which contains a translated human-readable
        description of the triggering event.
  For example, the trigger set for the 'node' module has 'node' as the
  outermost key and defines triggers for 'node_insert', 'node_update',
  'node_delete' etc. that fire when a node is saved, updated, etc.

@see hook_action_info()
@see hook_trigger_info_alter()
```

## Code

```php
function hook_trigger_info() {
  return array(
    'node' => array(
      'node_presave' => array(
        'label' => t('When either saving new content or updating existing content'),
      ),
      'node_insert' => array(
        'label' => t('After saving new content'),
      ),
      'node_update' => array(
        'label' => t('After saving updated content'),
      ),
      'node_delete' => array(
        'label' => t('After deleting content'),
      ),
      'node_view' => array(
        'label' => t('When content is viewed by an authenticated user'),
      ),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_trigger_info()".

- [actions_loop_test_trigger_info()](../../simpletest/tests/actions_loop_test.module/actions_loop_test_trigger_info.md) — `modules/simpletest/tests/actions_loop_test.module`
- [trigger_trigger_info()](../trigger.module/trigger_trigger_info.md) — `modules/trigger/trigger.module`
- [trigger_test_trigger_info()](../tests/trigger_test.module/trigger_test_trigger_info.md) — `modules/trigger/tests/trigger_test.module`

---
_Drupal 7.103 · [modules/trigger/trigger.api.php](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
