# image_field_instance_settings_form()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 72–166 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L72-L166)
- **Module/theme:** image
- **Implements:** [hook_field_instance_settings_form()](../../field_ui/field_ui.api.php/hook_field_instance_settings_form.md)

## Signature

```php
function image_field_instance_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_instance_settings_form().
```

## Code

```php
function image_field_instance_settings_form($field, $instance) {
  $settings = $instance['settings'];

  // Use the file field instance settings form as a basis.
  $form = file_field_instance_settings_form($field, $instance);

  // Add maximum and minimum resolution settings.
  $max_resolution = explode('x', $settings['max_resolution']) + array('', '');
  $form['max_resolution'] = array(
    '#type' => 'item',
    '#title' => t('Maximum image resolution'),
    '#element_validate' => array('_image_field_resolution_validate'),
    '#weight' => 4.1,
    '#field_prefix' => '<div class="container-inline">',
    '#field_suffix' => '</div>',
    '#description' => t('The maximum allowed image size expressed as WIDTHxHEIGHT (e.g. 640x480). Leave blank for no restriction. If a larger image is uploaded, it will be resized to reflect the given width and height. Resizing images on upload will cause the loss of <a href="http://en.wikipedia.org/wiki/Exchangeable_image_file_format">EXIF data</a> in the image.'),
  );
  $form['max_resolution']['x'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum width'),
    '#title_display' => 'invisible',
    '#default_value' => $max_resolution[0],
    '#size' => 5,
    '#maxlength' => 5,
    '#field_suffix' => ' x ',
  );
  $form['max_resolution']['y'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum height'),
    '#title_display' => 'invisible',
    '#default_value' => $max_resolution[1],
    '#size' => 5,
    '#maxlength' => 5,
    '#field_suffix' => ' ' . t('pixels'),
  );

  $min_resolution = explode('x', $settings['min_resolution']) + array('', '');
  $form['min_resolution'] = array(
    '#type' => 'item',
    '#title' => t('Minimum image resolution'),
    '#element_validate' => array('_image_field_resolution_validate'),
    '#weight' => 4.2,
    '#field_prefix' => '<div class="container-inline">',
    '#field_suffix' => '</div>',
    '#description' => t('The minimum allowed image size expressed as WIDTHxHEIGHT (e.g. 640x480). Leave blank for no restriction. If a smaller image is uploaded, it will be rejected.'),
  );
  $form['min_resolution']['x'] = array(
    '#type' => 'textfield',
    '#title' => t('Minimum width'),
    '#title_display' => 'invisible',
    '#default_value' => $min_resolution[0],
    '#size' => 5,
    '#maxlength' => 5,
    '#field_suffix' => ' x ',
  );
  $form['min_resolution']['y'] = array(
    '#type' => 'textfield',
    '#title' => t('Minimum height'),
    '#title_display' => 'invisible',
    '#default_value' => $min_resolution[1],
    '#size' => 5,
    '#maxlength' => 5,
    '#field_suffix' => ' ' . t('pixels'),
  );

  // Remove the description option.
  unset($form['description_field']);

  // Add title and alt configuration options.
  $form['alt_field'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable <em>Alt</em> field'),
    '#default_value' => $settings['alt_field'],
    '#description' => t('The alt attribute may be used by search engines, screen readers, and when the image cannot be loaded.'),
    '#weight' => 10,
  );
  $form['title_field'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable <em>Title</em> field'),
    '#default_value' => $settings['title_field'],
    '#description' => t('The title attribute is used as a tooltip when the mouse hovers over the image.'),
    '#weight' => 11,
  );

  // Add the default image to the instance.
  $form['default_image'] = array(
    '#title' => t('Default image'),
    '#type' => 'managed_file',
    '#description' => t("If no image is uploaded, this image will be shown on display and will override the field's default image."),
    '#default_value' => $settings['default_image'],
    '#upload_location' => $field['settings']['uri_scheme'] . '://default_images/',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
