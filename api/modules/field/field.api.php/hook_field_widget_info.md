# hook_field_widget_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 790–822 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L790-L822)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_info()
```

## Documentation

```text
Expose Field API widget types.

@return
  An array describing the widget types implemented by the module.
  The keys are widget type names. To avoid name clashes, widget type
  names should be prefixed with the name of the module that exposes them.
  The values are arrays describing the widget type, with the following
  key/value pairs:
  - label: The human-readable name of the widget type.
  - description: A short description for the widget type.
  - field types: An array of field types the widget supports.
  - settings: An array whose keys are the names of the settings available
    for the widget type, and whose values are the default values for those
    settings.
  - behaviors: (optional) An array describing behaviors of the widget, with
    the following elements:
    - multiple values: One of the following constants:
      - FIELD_BEHAVIOR_DEFAULT: (default) If the widget allows the input of
        one single field value (most common case). The widget will be
        repeated for each value input.
      - FIELD_BEHAVIOR_CUSTOM: If one single copy of the widget can receive
        several field values. Examples: checkboxes, multiple select,
        comma-separated textfield.
    - default value: One of the following constants:
      - FIELD_BEHAVIOR_DEFAULT: (default) If the widget accepts default
        values.
      - FIELD_BEHAVIOR_NONE: if the widget does not support default values.
  - weight: (optional) An integer to determine the weight of this widget
    relative to other widgets in the Field UI when selecting a widget for a
    given field instance.

@see hook_field_widget_info_alter()
@see hook_field_widget_form()
@see hook_field_widget_form_alter()
@see hook_field_widget_WIDGET_TYPE_form_alter()
@see hook_field_widget_error()
@see hook_field_widget_settings_form()
```

## Code

```php
function hook_field_widget_info() {
  return array(
    'text_textfield' => array(
      'label' => t('Text field'),
      'field types' => array('text'),
      'settings' => array('size' => 60),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_DEFAULT,
        'default value' => FIELD_BEHAVIOR_DEFAULT,
      ),
    ),
    'text_textarea' => array(
      'label' => t('Text area (multiple rows)'),
      'field types' => array('text_long'),
      'settings' => array('rows' => 5),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_DEFAULT,
        'default value' => FIELD_BEHAVIOR_DEFAULT,
      ),
    ),
    'text_textarea_with_summary' => array(
      'label' => t('Text area with a summary'),
      'field types' => array('text_with_summary'),
      'settings' => array('rows' => 20, 'summary_rows' => 5),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_DEFAULT,
        'default value' => FIELD_BEHAVIOR_DEFAULT,
      ),
      // As an advanced widget, force it to sink to the bottom of the choices.
      'weight' => 2,
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_info()".

- [field_test_field_widget_info()](../tests/field_test.field.inc/field_test_field_widget_info.md) — `modules/field/tests/field_test.field.inc`
- [file_field_widget_info()](../../file/file.field.inc/file_field_widget_info.md) — `modules/file/file.field.inc`
- [image_field_widget_info()](../../image/image.field.inc/image_field_widget_info.md) — `modules/image/image.field.inc`
- [number_field_widget_info()](../modules/number/number.module/number_field_widget_info.md) — `modules/field/modules/number/number.module`
- [options_field_widget_info()](../modules/options/options.module/options_field_widget_info.md) — `modules/field/modules/options/options.module`
- [taxonomy_field_widget_info()](../../taxonomy/taxonomy.module/taxonomy_field_widget_info.md) — `modules/taxonomy/taxonomy.module`
- [text_field_widget_info()](../modules/text/text.module/text_field_widget_info.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
