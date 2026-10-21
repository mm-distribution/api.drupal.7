# system_actions_manage_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3095–3099 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3095-L3099)
- **Module/theme:** system

## Signature

```php
function system_actions_manage_form_submit($form, &$form_state)
```

## Documentation

```text
Process system_actions_manage form submissions.

@see system_actions_manage_form()
```

## Code

```php
function system_actions_manage_form_submit($form, &$form_state) {
  if ($form_state['values']['action']) {
    $form_state['redirect'] = 'admin/config/system/actions/configure/' . $form_state['values']['action'];
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
