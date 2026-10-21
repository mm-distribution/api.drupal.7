# image_field_info()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 11–34 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L11-L34)
- **Module/theme:** image
- **Implements:** [hook_field_info()](../../field/field.api.php/hook_field_info.md)

## Signature

```php
function image_field_info()
```

## Documentation

```text
Implements hook_field_info().
```

## Code

```php
function image_field_info() {
  return array(
    'image' => array(
      'label' => t('Image'),
      'description' => t('This field stores the ID of an image file as an integer value.'),
      'settings' => array(
        'uri_scheme' => variable_get('file_default_scheme', 'public'),
        'default_image' => 0,
      ),
      'instance_settings' => array(
        'file_extensions' => 'png gif jpg jpeg',
        'file_directory' => '[date:custom:Y]-[date:custom:m]',
        'max_filesize' => '',
        'alt_field' => 0,
        'title_field' => 0,
        'max_resolution' => '',
        'min_resolution' => '',
        'default_image' => 0,
      ),
      'default_widget' => 'image_image',
      'default_formatter' => 'image',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
