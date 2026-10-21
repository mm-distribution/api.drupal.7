# field_ui_default_value_widget()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1995–2019 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1995-L2019)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_default_value_widget($field, $instance, &$form, &$form_state)
```

## Documentation

```text
Builds the default value fieldset for a given field instance.
```

## Code

```php
function field_ui_default_value_widget($field, $instance, &$form, &$form_state) {
  $field_name = $field['field_name'];

  $element = array(
    '#type' => 'fieldset',
    '#title' => t('Default value'),
    '#collapsible' => FALSE,
    '#tree' => TRUE,
    '#description' => t('The default value for this field, used when creating new content.'),
    // Stick to an empty 'parents' on this form in order not to breaks widgets
    // that do not use field_widget_[field|instance]() and still access
    // $form_state['field'] directly.
    '#parents' => array(),
  );

  // Insert the widget.
  $items = $instance['default_value'];
  $instance['required'] = FALSE;
  $instance['description'] = '';

  // @todo Allow multiple values (requires more work on 'add more' JS handler).
  $element += field_default_form($instance['entity_type'], NULL, $field, $instance, LANGUAGE_NONE, $items, $element, $form_state, 0);

  return $element;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
