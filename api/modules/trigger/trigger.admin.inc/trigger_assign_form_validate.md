# trigger_assign_form_validate()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 212–224 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L212-L224)
- **Module/theme:** trigger

## Signature

```php
function trigger_assign_form_validate($form, $form_state)
```

## Documentation

```text
Form validation handler for trigger_assign_form().

Makes sure that the user is not re-assigning an action to an event.

@see trigger_assign_form_submit()
```

## Code

```php
function trigger_assign_form_validate($form, $form_state) {
  $form_values = $form_state['values'];
  if (!empty($form_values['aid'])) {
    $aid = actions_function_lookup($form_values['aid']);
    $aid_exists = db_query("SELECT aid FROM {trigger_assignments} WHERE hook = :hook AND aid = :aid", array(
      ':hook' => $form_values['hook'],
      ':aid' => $aid,
    ))->fetchField();
    if ($aid_exists) {
      form_set_error($form_values['hook'], t('The action you chose is already assigned to that trigger.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
