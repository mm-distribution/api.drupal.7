# system_date_delete_format_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2842–2849 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2842-L2849)
- **Module/theme:** system

## Signature

```php
function system_date_delete_format_form_submit($form, &$form_state)
```

## Documentation

```text
Delete a configured date format.
```

## Code

```php
function system_date_delete_format_form_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    $format = system_get_date_format($form_state['values']['dfid']);
    system_date_format_delete($form_state['values']['dfid']);
    drupal_set_message(t('Removed date format %format.', array('%format' => format_date(REQUEST_TIME, 'custom', $format->format))));
    $form_state['redirect'] = 'admin/config/regional/date-time/formats';
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
