# system_add_date_format_type_form_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2186–2196 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2186-L2196)
- **Module/theme:** system

## Signature

```php
function system_add_date_format_type_form_validate($form, &$form_state)
```

## Documentation

```text
Validate system_add_date_format_type form submissions.
```

## Code

```php
function system_add_date_format_type_form_validate($form, &$form_state) {
  if (!empty($form_state['values']['machine_name']) && !empty($form_state['values']['date_type'])) {
    if (!preg_match("/^[a-zA-Z0-9_]+$/", trim($form_state['values']['machine_name']))) {
      form_set_error('machine_name', t('The date type must contain only alphanumeric characters and underscores.'));
    }
    $types = system_get_date_types();
    if (in_array(trim($form_state['values']['machine_name']), array_keys($types))) {
      form_set_error('machine_name', t('This date type already exists. Enter a unique type.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
