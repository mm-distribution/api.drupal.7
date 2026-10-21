# _color_save_stylesheet()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 567–573 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L567-L573)
- **Module/theme:** color

## Signature

```php
function _color_save_stylesheet($file, $style, &$paths)
```

## Documentation

```text
Saves the rewritten stylesheet to disk.
```

## Code

```php
function _color_save_stylesheet($file, $style, &$paths) {
  $filepath = file_unmanaged_save_data($style, $file, FILE_EXISTS_REPLACE);
  $paths['files'][] = $filepath;

  // Set standard file permissions for webserver-generated files.
  drupal_chmod($file);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
