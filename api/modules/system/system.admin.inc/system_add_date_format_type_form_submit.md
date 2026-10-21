# system_add_date_format_type_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2201–2214 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2201-L2214)
- **Module/theme:** system

## Signature

```php
function system_add_date_format_type_form_submit($form, &$form_state)
```

## Documentation

```text
Process system_add_date_format_type form submissions.
```

## Code

```php
function system_add_date_format_type_form_submit($form, &$form_state) {
  $machine_name = trim($form_state['values']['machine_name']);

  $format_type = array();
  $format_type['title'] = trim($form_state['values']['date_type']);
  $format_type['type'] = $machine_name;
  $format_type['locked'] = 0;
  $format_type['is_new'] = 1;
  system_date_format_type_save($format_type);
  variable_set('date_format_' . $machine_name, $form_state['values']['date_format']);

  drupal_set_message(t('New date type added successfully.'));
  $form_state['redirect'] = 'admin/config/regional/date-time';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
