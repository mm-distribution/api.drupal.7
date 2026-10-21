# filter_admin_format_form_validate()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 330–342 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L330-L342)
- **Module/theme:** filter

## Signature

```php
function filter_admin_format_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for filter_admin_format_form().

@see filter_admin_format_form_submit()
```

## Code

```php
function filter_admin_format_form_validate($form, &$form_state) {
  $format_format = trim($form_state['values']['format']);
  $format_name = trim($form_state['values']['name']);

  // Ensure that the values to be saved later are exactly the ones validated.
  form_set_value($form['format'], $format_format, $form_state);
  form_set_value($form['name'], $format_name, $form_state);

  $result = db_query("SELECT format FROM {filter_format} WHERE name = :name AND format <> :format", array(':name' => $format_name, ':format' => $format_format))->fetchField();
  if ($result) {
    form_set_error('name', t('Text format names must be unique. A format named %name already exists.', array('%name' => $format_name)));
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
