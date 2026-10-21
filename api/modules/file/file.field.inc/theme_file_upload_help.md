# theme_file_upload_help()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 940–970 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L940-L970)
- **Module/theme:** file
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_file_upload_help($variables)
```

## Documentation

```text
Returns HTML for help text based on file upload validators.

@param $variables
  An associative array containing:
  - description: The normal description for this field, specified by the
    user.
  - upload_validators: An array of upload validators as used in
    $element['#upload_validators'].

@ingroup themeable
```

## Code

```php
function theme_file_upload_help($variables) {
  $description = $variables['description'];
  $upload_validators = $variables['upload_validators'];

  $descriptions = array();

  if (!empty($description)) {
    $descriptions[] = $description;
  }
  if (isset($upload_validators['file_validate_size'])) {
    $descriptions[] = t('Files must be less than !size.', array('!size' => '<strong>' . format_size($upload_validators['file_validate_size'][0]) . '</strong>'));
  }
  if (isset($upload_validators['file_validate_extensions'])) {
    $descriptions[] = t('Allowed file types: !extensions.', array('!extensions' => '<strong>' . check_plain($upload_validators['file_validate_extensions'][0]) . '</strong>'));
  }
  if (isset($upload_validators['file_validate_image_resolution'])) {
    $max = $upload_validators['file_validate_image_resolution'][0];
    $min = $upload_validators['file_validate_image_resolution'][1];
    if ($min && $max) {
      $descriptions[] = t('Images must be at least !min pixels. Images larger than !max pixels will be resized.', array('!min' => '<strong>' . $min . '</strong>', '!max' => '<strong>' . $max . '</strong>'));
    }
    elseif ($min) {
      $descriptions[] = t('Images must be at least !min pixels.', array('!min' => '<strong>' . $min . '</strong>'));
    }
    elseif ($max) {
      $descriptions[] = t('Images larger than !max pixels will be resized.', array('!max' => '<strong>' . $max . '</strong>'));
    }
  }

  return implode('<br />', $descriptions);
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
