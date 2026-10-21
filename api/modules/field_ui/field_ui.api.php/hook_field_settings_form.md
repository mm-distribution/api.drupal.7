# hook_field_settings_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/field_ui/field_ui.api.php`](_file.md), lines 38–49 · [local source](../../../../source/modules/field_ui/field_ui.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php#L38-L49)
- **Module/theme:** field_ui
- **Topics:** [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Add settings to a field settings form.

Invoked from field_ui_field_settings_form() to allow the module defining the
field to add global settings (i.e. settings that do not depend on the bundle
or instance) to the field settings form. If the field already has data, only
include settings that are safe to change.

@todo: Only the field type module knows which settings will affect the
field's schema, but only the field storage module knows what schema
changes are permitted once a field already has data. Probably we need an
easy way for a field type module to ask whether an update to a new schema
will be allowed without having to build up a fake $prior_field structure
for hook_field_update_forbid().

@param $field
  The field structure being configured.
@param $instance
  The instance structure being configured.
@param $has_data
  TRUE if the field already has data, FALSE if not.

@return
  The form definition for the field settings.
```

## Code

```php
function hook_field_settings_form($field, $instance, $has_data) {
  $settings = $field['settings'];
  $form['max_length'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum length'),
    '#default_value' => $settings['max_length'],
    '#required' => FALSE,
    '#element_validate' => array('element_validate_integer_positive'),
    '#description' => t('The maximum length of the field in characters. Leave blank for an unlimited size.'),
  );
  return $form;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_settings_form()".

- [field_test_field_settings_form()](../../field/tests/field_test.field.inc/field_test_field_settings_form.md) — `modules/field/tests/field_test.field.inc`
- [file_field_settings_form()](../../file/file.field.inc/file_field_settings_form.md) — `modules/file/file.field.inc`
- [image_field_settings_form()](../../image/image.field.inc/image_field_settings_form.md) — `modules/image/image.field.inc`
- [list_field_settings_form()](../../field/modules/list/list.module/list_field_settings_form.md) — `modules/field/modules/list/list.module`
- [number_field_settings_form()](../../field/modules/number/number.module/number_field_settings_form.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_settings_form()](../../taxonomy/taxonomy.module/taxonomy_field_settings_form.md) — `modules/taxonomy/taxonomy.module`
- [text_field_settings_form()](../../field/modules/text/text.module/text_field_settings_form.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field_ui/field_ui.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
