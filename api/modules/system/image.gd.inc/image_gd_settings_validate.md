# image_gd_settings_validate()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 44–50 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L44-L50)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_settings_validate($form, &$form_state)
```

## Documentation

```text
Validate the submitted GD settings.
```

## Code

```php
function image_gd_settings_validate($form, &$form_state) {
  // Validate image quality range.
  $value = $form_state['values']['image_jpeg_quality'];
  if (!is_numeric($value) || $value < 0 || $value > 100) {
    form_set_error('image_jpeg_quality', t('JPEG quality must be a number between 0 and 100.'));
  }
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
