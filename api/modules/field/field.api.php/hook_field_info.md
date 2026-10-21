# hook_field_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 160–187 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L160-L187)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_info()
```

## Documentation

```text
Define Field API field types.

Along with this hook, you also need to implement other hooks. See
@link field_types Field Types API @endlink for more information.

@return
  An array whose keys are field type names and whose values are arrays
  describing the field type, with the following key/value pairs:
  - label: The human-readable name of the field type.
  - description: A short description for the field type.
  - settings: An array whose keys are the names of the settings available
    for the field type, and whose values are the default values for those
    settings.
  - instance_settings: An array whose keys are the names of the settings
    available for instances of the field type, and whose values are the
    default values for those settings. Instance-level settings can have
    different values on each field instance, and thus allow greater
    flexibility than field-level settings. It is recommended to put settings
    at the instance level whenever possible. Notable exceptions: settings
    acting on the schema definition, or settings that Views needs to use
    across field instances (for example, the list of allowed values).
  - default_widget: The machine name of the default widget to be used by
    instances of this field type, when no widget is specified in the
    instance definition. This widget must be available whenever the field
    type is available (i.e. provided by the field type module, or by a module
    the field type module depends on).
  - default_formatter: The machine name of the default formatter to be used
    by instances of this field type, when no formatter is specified in the
    instance definition. This formatter must be available whenever the field
    type is available (i.e. provided by the field type module, or by a module
    the field type module depends on).
  - no_ui: (optional) A boolean specifying that users should not be allowed
    to create fields and instances of this field type through the UI. Such
    fields can only be created programmatically with field_create_field()
    and field_create_instance(). Defaults to FALSE.

@see hook_field_info_alter()
```

## Code

```php
function hook_field_info() {
  return array(
    'text' => array(
      'label' => t('Text'),
      'description' => t('This field stores varchar text in the database.'),
      'settings' => array('max_length' => 255),
      'instance_settings' => array('text_processing' => 0),
      'default_widget' => 'text_textfield',
      'default_formatter' => 'text_default',
    ),
    'text_long' => array(
      'label' => t('Long text'),
      'description' => t('This field stores long text in the database.'),
      'settings' => array('max_length' => ''),
      'instance_settings' => array('text_processing' => 0),
      'default_widget' => 'text_textarea',
      'default_formatter' => 'text_default',
    ),
    'text_with_summary' => array(
      'label' => t('Long text and summary'),
      'description' => t('This field stores long text in the database along with optional summary text.'),
      'settings' => array('max_length' => ''),
      'instance_settings' => array('text_processing' => 1, 'display_summary' => 0),
      'default_widget' => 'text_textarea_with_summary',
      'default_formatter' => 'text_summary_or_trimmed',
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_info()".

- [field_test_field_info()](../tests/field_test.field.inc/field_test_field_info.md) — `modules/field/tests/field_test.field.inc`
- [file_field_info()](../../file/file.field.inc/file_field_info.md) — `modules/file/file.field.inc`
- [image_field_info()](../../image/image.field.inc/image_field_info.md) — `modules/image/image.field.inc`
- [list_field_info()](../modules/list/list.module/list_field_info.md) — `modules/field/modules/list/list.module`
- [number_field_info()](../modules/number/number.module/number_field_info.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_info()](../../taxonomy/taxonomy.module/taxonomy_field_info.md) — `modules/taxonomy/taxonomy.module`
- [text_field_info()](../modules/text/text.module/text_field_info.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
