# text_field_widget_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 483–507 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L483-L507)
- **Module/theme:** text
- **Implements:** [hook_field_widget_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_widget_settings_form.md)

## Signature

```php
function text_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_widget_settings_form().
```

## Code

```php
function text_field_widget_settings_form($field, $instance) {
  $widget = $instance['widget'];
  $settings = $widget['settings'];

  if ($widget['type'] == 'text_textfield') {
    $form['size'] = array(
      '#type' => 'textfield',
      '#title' => t('Size of textfield'),
      '#default_value' => $settings['size'],
      '#required' => TRUE,
      '#element_validate' => array('element_validate_integer_positive'),
    );
  }
  else {
    $form['rows'] = array(
      '#type' => 'textfield',
      '#title' => t('Rows'),
      '#default_value' => $settings['rows'],
      '#required' => TRUE,
      '#element_validate' => array('element_validate_integer_positive'),
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
