# system_add_date_formats_form_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2969–2975 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2969-L2975)
- **Module/theme:** system

## Signature

```php
function system_add_date_formats_form_validate($form, &$form_state)
```

## Documentation

```text
Validate new date format string submission.
```

## Code

```php
function system_add_date_formats_form_validate($form, &$form_state) {
  $formats = system_get_date_formats('custom');
  $format = trim($form_state['values']['date_format']);
  if (!empty($formats) && in_array($format, array_keys($formats)) && (!isset($form_state['values']['dfid']) || $form_state['values']['dfid'] != $formats[$format]['dfid'])) {
    form_set_error('date_format', t('This format already exists. Enter a unique format string.'));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
