# image_field_formatter_settings_form()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 499–525 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L499-L525)
- **Module/theme:** image
- **Implements:** [hook_field_formatter_settings_form()](../../field_ui/field_ui.api.php/hook_field_formatter_settings_form.md)

## Signature

```php
function image_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_formatter_settings_form().
```

## Code

```php
function image_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $image_styles = image_style_options(FALSE, PASS_THROUGH);
  $element['image_style'] = array(
    '#title' => t('Image style'),
    '#type' => 'select',
    '#default_value' => $settings['image_style'],
    '#empty_option' => t('None (original image)'),
    '#options' => $image_styles,
  );

  $link_types = array(
    'content' => t('Content'),
    'file' => t('File'),
  );
  $element['image_link'] = array(
    '#title' => t('Link image to'),
    '#type' => 'select',
    '#default_value' => $settings['image_link'],
    '#empty_option' => t('Nothing'),
    '#options' => $link_types,
  );

  return $element;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
