# system_delete_date_format_type_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2854–2870 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2854-L2870)
- **Module/theme:** system

## Signature

```php
function system_delete_date_format_type_form($form, &$form_state, $format_type)
```

## Documentation

```text
Menu callback; present a form for deleting a date type.
```

## Code

```php
function system_delete_date_format_type_form($form, &$form_state, $format_type) {
  $form['format_type'] = array(
    '#type' => 'value',
    '#value' => $format_type,
  );
  $type_info = system_get_date_types($format_type);

  $output = confirm_form($form,
    t('Are you sure you want to remove the date type %type?', array('%type' => $type_info['title'])),
    'admin/config/regional/date-time',
    t('This action cannot be undone.'),
    t('Remove'), t('Cancel'),
    'confirm'
  );

  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
