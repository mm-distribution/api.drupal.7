# trigger_unassign_submit()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 89–105 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L89-L105)
- **Module/theme:** trigger

## Signature

```php
function trigger_unassign_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for trigger_unassign().
```

## Code

```php
function trigger_unassign_submit($form, &$form_state) {
  if ($form_state['values']['confirm'] == 1) {
    $aid = actions_function_lookup($form_state['values']['aid']);
    db_delete('trigger_assignments')
      ->condition('hook', $form_state['values']['hook'])
      ->condition('aid', $aid)
      ->execute();
    drupal_static_reset('trigger_get_assigned_actions');
    $actions = actions_get_all_actions();
    watchdog('actions', 'Action %action has been unassigned.',  array('%action' => $actions[$aid]['label']));
    drupal_set_message(t('Action %action has been unassigned.', array('%action' => $actions[$aid]['label'])));
    $form_state['redirect'] = 'admin/structure/trigger/' . $form_state['values']['module'];
  }
  else {
    drupal_goto('admin/structure/trigger');
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
