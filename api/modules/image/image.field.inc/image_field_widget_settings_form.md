# image_field_widget_settings_form()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 308–326 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L308-L326)
- **Module/theme:** image
- **Implements:** [hook_field_widget_settings_form()](../../field_ui/field_ui.api.php/hook_field_widget_settings_form.md)

## Signature

```php
function image_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_widget_settings_form().
```

## Code

```php
function image_field_widget_settings_form($field, $instance) {
  $widget = $instance['widget'];
  $settings = $widget['settings'];

  // Use the file widget settings form.
  $form = file_field_widget_settings_form($field, $instance);

  $form['preview_image_style'] = array(
    '#title' => t('Preview image style'),
    '#type' => 'select',
    '#options' => image_style_options(FALSE, PASS_THROUGH),
    '#empty_option' => '<' . t('no preview') . '>',
    '#default_value' => $settings['preview_image_style'],
    '#description' => t('The preview image will be shown while editing the content.'),
    '#weight' => 15,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
