# image_field_formatter_info()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 484–494 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L484-L494)
- **Module/theme:** image
- **Implements:** [hook_field_formatter_info()](../../field/field.api.php/hook_field_formatter_info.md)

## Signature

```php
function image_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function image_field_formatter_info() {
  $formatters = array(
    'image' => array(
      'label' => t('Image'),
      'field types' => array('image'),
      'settings' => array('image_style' => '', 'image_link' => ''),
    ),
  );

  return $formatters;
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
