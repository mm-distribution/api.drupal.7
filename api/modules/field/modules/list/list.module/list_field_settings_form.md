# list_field_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 60–155 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L60-L155)
- **Module/theme:** list
- **Implements:** [hook_field_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_settings_form.md)

## Signature

```php
function list_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Implements hook_field_settings_form().
```

## Code

```php
function list_field_settings_form($field, $instance, $has_data) {
  $settings = $field['settings'];

  switch ($field['type']) {
    case 'list_integer':
    case 'list_float':
    case 'list_text':
      $form['allowed_values'] = array(
        '#type' => 'textarea',
        '#title' => t('Allowed values list'),
        '#default_value' => empty($settings['allowed_values_function']) ? list_allowed_values_string($settings['allowed_values']) : '',
        '#rows' => 10,
        '#element_validate' => array('list_allowed_values_setting_validate'),
        '#field_has_data' => $has_data,
        '#field' => $field,
        '#field_type' => $field['type'],
        '#access' => empty($settings['allowed_values_function']),
      );

      $description = '<p>' . t('The possible values this field can contain. Enter one value per line, in the format key|label.');
      if ($field['type'] == 'list_integer' || $field['type'] == 'list_float') {
        $description .= '<br/>' . t('The key is the stored value, and must be numeric. The label will be used in displayed values and edit forms.');
        $description .= '<br/>' . t('The label is optional: if a line contains a single number, it will be used as key and label.');
        $description .= '<br/>' . t('Lists of labels are also accepted (one label per line), only if the field does not hold any values yet. Numeric keys will be automatically generated from the positions in the list.');
      }
      else {
        $description .= '<br/>' . t('The key is the stored value. The label will be used in displayed values and edit forms.');
        $description .= '<br/>' . t('The label is optional: if a line contains a single string, it will be used as key and label.');
      }
      $description .= '</p>';
      $form['allowed_values']['#description'] = $description;

      break;

    case 'list_boolean':
      $values = $settings['allowed_values'];
      $off_value = array_shift($values);
      $on_value = array_shift($values);

      $form['allowed_values'] = array(
        '#type' => 'value',
        '#description' => '',
        '#value_callback' => 'list_boolean_allowed_values_callback',
        '#access' => empty($settings['allowed_values_function']),
      );
      $form['allowed_values']['on'] = array(
        '#type' => 'textfield',
        '#title' => t('On value'),
        '#default_value' => $on_value,
        '#required' => FALSE,
        '#description' => t('If left empty, "1" will be used.'),
        // Change #parents to make sure the element is not saved into field
        // settings.
        '#parents' => array('on'),
      );
      $form['allowed_values']['off'] = array(
        '#type' => 'textfield',
        '#title' => t('Off value'),
        '#default_value' => $off_value,
        '#required' => FALSE,
        '#description' => t('If left empty, "0" will be used.'),
        // Change #parents to make sure the element is not saved into field
        // settings.
        '#parents' => array('off'),
      );

      // Link the allowed value to the on / off elements to prepare for the rare
      // case of an alter changing #parents.
      $form['allowed_values']['#on_parents'] = &$form['allowed_values']['on']['#parents'];
      $form['allowed_values']['#off_parents'] = &$form['allowed_values']['off']['#parents'];

      break;
  }

  // Alter the description for allowed values depending on the widget type.
  if ($instance['widget']['type'] == 'options_onoff') {
    $form['allowed_values']['#description'] .= '<p>' . t("For a 'single on/off checkbox' widget, define the 'off' value first, then the 'on' value in the <strong>Allowed values</strong> section. Note that the checkbox will be labeled with the label of the 'on' value.") . '</p>';
  }
  elseif ($instance['widget']['type'] == 'options_buttons') {
    $form['allowed_values']['#description'] .= '<p>' . t("The 'checkboxes/radio buttons' widget will display checkboxes if the <em>Number of values</em> option is greater than 1 for this field, otherwise radios will be displayed.") . '</p>';
  }
  $form['allowed_values']['#description'] .= '<p>' . t('Allowed HTML tags in labels: @tags', array('@tags' => _field_filter_xss_display_allowed_tags())) . '</p>';

  $form['allowed_values_function'] = array(
    '#type' => 'value',
    '#value' => $settings['allowed_values_function'],
  );
  $form['allowed_values_function_display'] = array(
    '#type' => 'item',
    '#title' => t('Allowed values list'),
    '#markup' => t('The value of this field is being determined by the %function function and may not be changed.', array('%function' => $settings['allowed_values_function'])),
    '#access' => !empty($settings['allowed_values_function']),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
