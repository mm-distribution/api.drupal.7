# image_field_widget_info()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 288–303 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L288-L303)
- **Module/theme:** image
- **Implements:** [hook_field_widget_info()](../../field/field.api.php/hook_field_widget_info.md)

## Signature

```php
function image_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function image_field_widget_info() {
  return array(
    'image_image' => array(
      'label' => t('Image'),
      'field types' => array('image'),
      'settings' => array(
        'progress_indicator' => 'throbber',
        'preview_image_style' => 'thumbnail',
      ),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
        'default value' => FIELD_BEHAVIOR_NONE,
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
