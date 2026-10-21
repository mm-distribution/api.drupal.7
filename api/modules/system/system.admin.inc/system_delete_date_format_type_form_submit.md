# system_delete_date_format_type_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2875–2882 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2875-L2882)
- **Module/theme:** system

## Signature

```php
function system_delete_date_format_type_form_submit($form, &$form_state)
```

## Documentation

```text
Delete a configured date type.
```

## Code

```php
function system_delete_date_format_type_form_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    $type_info = system_get_date_types($form_state['values']['format_type']);
    system_date_format_type_delete($form_state['values']['format_type']);
    drupal_set_message(t('Removed date type %type.', array('%type' => $type_info['title'])));
    $form_state['redirect'] = 'admin/config/regional/date-time';
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
