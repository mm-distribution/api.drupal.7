# image_gd_settings()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 16–39 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L16-L39)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_settings()
```

## Documentation

```text
Retrieve settings for the GD2 toolkit.
```

## Code

```php
function image_gd_settings() {
  if (image_gd_check_settings()) {
    $form['status'] = array(
      '#markup' => t('The GD toolkit is installed and working properly.')
    );

    $form['image_jpeg_quality'] = array(
      '#type' => 'textfield',
      '#title' => t('JPEG quality'),
      '#description' => t('Define the image quality for JPEG manipulations. Ranges from 0 to 100. Higher values mean better image quality but bigger files.'),
      '#size' => 10,
      '#maxlength' => 3,
      '#default_value' => variable_get('image_jpeg_quality', 75),
      '#field_suffix' => t('%'),
    );
    $form['#element_validate'] = array('image_gd_settings_validate');

    return $form;
  }
  else {
    form_set_error('image_toolkit', t('The GD image toolkit requires that the GD module for PHP be installed and configured properly. For more information see <a href="@url">PHP\'s image documentation</a>.', array('@url' => 'http://php.net/image')));
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
