# image_path_flush()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 548–556 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L548-L556)
- **Module/theme:** image

## Signature

```php
function image_path_flush($path)
```

## Documentation

```text
Clears cached versions of a specific file in all styles.

@param $path
  The Drupal file path to the original image.
```

## Code

```php
function image_path_flush($path) {
  $styles = image_styles();
  foreach ($styles as $style) {
    $image_path = image_style_path($style['name'], $path);
    if (file_exists($image_path)) {
      file_unmanaged_delete($image_path);
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
