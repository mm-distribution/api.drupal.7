# system_actions_delete_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3242–3249 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3242-L3249)
- **Module/theme:** system

## Signature

```php
function system_actions_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Process system_actions_delete form submissions.

Post-deletion operations for action deletion.
```

## Code

```php
function system_actions_delete_form_submit($form, &$form_state) {
  $aid = $form_state['values']['aid'];
  $action = actions_load($aid);
  actions_delete($aid);
  watchdog('user', 'Deleted action %aid (%action)', array('%aid' => $aid, '%action' => $action->label));
  drupal_set_message(t('Action %action was deleted', array('%action' => $action->label)));
  $form_state['redirect'] = 'admin/config/system/actions/manage';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
