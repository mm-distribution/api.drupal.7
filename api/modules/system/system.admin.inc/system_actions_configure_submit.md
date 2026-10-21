# system_actions_configure_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3203–3215 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3203-L3215)
- **Module/theme:** system

## Signature

```php
function system_actions_configure_submit($form, &$form_state)
```

## Documentation

```text
Process system_actions_configure() form submissions.
```

## Code

```php
function system_actions_configure_submit($form, &$form_state) {
  $function = actions_function_lookup($form_state['values']['actions_action']);
  $submit_function = $function . '_submit';

  // Action will return keyed array of values to store.
  $params = $submit_function($form, $form_state);
  $aid = isset($form_state['values']['actions_aid']) ? $form_state['values']['actions_aid'] : NULL;

  actions_save($function, $form_state['values']['actions_type'], $params, $form_state['values']['actions_label'], $aid);
  drupal_set_message(t('The action has been successfully saved.'));

  $form_state['redirect'] = 'admin/config/system/actions/manage';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
