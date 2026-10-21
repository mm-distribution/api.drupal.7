# image_field_widget_process()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 373–448 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L373-L448)
- **Module/theme:** image

## Signature

```php
function image_field_widget_process($element, &$form_state, $form)
```

## Documentation

```text
An element #process callback for the image_image field type.

Expands the image_image type to include the alt and title fields.
```

## Code

```php
function image_field_widget_process($element, &$form_state, $form) {
  $item = $element['#value'];
  $item['fid'] = $element['fid']['#value'];

  $instance = field_widget_instance($element, $form_state);

  $settings = $instance['settings'];
  $widget_settings = $instance['widget']['settings'];

  $element['#theme'] = 'image_widget';
  $element['#attached']['css'][] = drupal_get_path('module', 'image') . '/image.css';

  // Add the image preview.
  if ($element['#file'] && $widget_settings['preview_image_style']) {
    $variables = array(
      'style_name' => $widget_settings['preview_image_style'],
      'path' => $element['#file']->uri,
    );

    // Determine image dimensions.
    if (isset($element['#value']['width']) && isset($element['#value']['height'])) {
      $variables['width'] = $element['#value']['width'];
      $variables['height'] = $element['#value']['height'];
    }
    else {
      $info = image_get_info($element['#file']->uri);

      if (is_array($info)) {
        $variables['width'] = $info['width'];
        $variables['height'] = $info['height'];
      }
      else {
        $variables['width'] = $variables['height'] = NULL;
      }
    }

    $element['preview'] = array(
      '#type' => 'markup',
      '#markup' => theme('image_style', $variables),
    );

    // Store the dimensions in the form so the file doesn't have to be accessed
    // again. This is important for remote files.
    $element['width'] = array(
      '#type' => 'hidden',
      '#value' => $variables['width'],
    );
    $element['height'] = array(
      '#type' => 'hidden',
      '#value' => $variables['height'],
    );
  }

  // Add the additional alt and title fields.
  $element['alt'] = array(
    '#title' => t('Alternate text'),
    '#type' => 'textfield',
    '#default_value' => isset($item['alt']) ? $item['alt'] : '',
    '#description' => t('This text will be used by screen readers, search engines, or when the image cannot be loaded.'),
    // @see http://www.gawds.org/show.php?contentid=28
    '#maxlength' => 512,
    '#weight' => -2,
    '#access' => (bool) $item['fid'] && $settings['alt_field'],
  );
  $element['title'] = array(
    '#type' => 'textfield',
    '#title' => t('Title'),
    '#default_value' => isset($item['title']) ? $item['title'] : '',
    '#description' => t('The title is used as a tool tip when the user hovers the mouse over the image.'),
    '#maxlength' => 1024,
    '#weight' => -1,
    '#access' => (bool) $item['fid'] && $settings['title_field'],
  );

  return $element;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
