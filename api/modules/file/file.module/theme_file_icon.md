# theme_file_icon()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 862–870 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L862-L870)
- **Module/theme:** file
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_file_icon($variables)
```

## Documentation

```text
Returns HTML for an image with an appropriate icon for the given file.

@param $variables
  An associative array containing:
  - file: A file object for which to make an icon.
  - icon_directory: (optional) A path to a directory of icons to be used for
    files. Defaults to the value of the "file_icon_directory" variable.
  - alt: (optional) The alternative text to represent the icon in text-based
    browsers. Defaults to an empty string.

@ingroup themeable
```

## Code

```php
function theme_file_icon($variables) {
  $file = $variables['file'];
  $alt = $variables['alt'];
  $icon_directory = $variables['icon_directory'];

  $mime = check_plain($file->filemime);
  $icon_url = file_icon_url($file, $icon_directory);
  return '<img class="file-icon" alt="' . check_plain($alt) . '" title="' . $mime . '" src="' . $icon_url . '" />';
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
