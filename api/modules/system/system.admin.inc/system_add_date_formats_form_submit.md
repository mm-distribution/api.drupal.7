# system_add_date_formats_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2980–2996 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2980-L2996)
- **Module/theme:** system

## Signature

```php
function system_add_date_formats_form_submit($form, &$form_state)
```

## Documentation

```text
Process new date format string submission.
```

## Code

```php
function system_add_date_formats_form_submit($form, &$form_state) {
  $format = array();
  $format['format'] = trim($form_state['values']['date_format']);
  $format['type'] = 'custom';
  $format['locked'] = 0;
  if (!empty($form_state['values']['dfid'])) {
    system_date_format_save($format, $form_state['values']['dfid']);
    drupal_set_message(t('Custom date format updated.'));
  }
  else {
    $format['is_new'] = 1;
    system_date_format_save($format);
    drupal_set_message(t('Custom date format added.'));
  }

  $form_state['redirect'] = 'admin/config/regional/date-time/formats';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
