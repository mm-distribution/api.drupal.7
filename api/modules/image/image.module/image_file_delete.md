# image_file_delete()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 338–341 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L338-L341)
- **Module/theme:** image
- **Implements:** [hook_file_delete()](../../system/system.api.php/hook_file_delete.md)

## Signature

```php
function image_file_delete($file)
```

## Documentation

```text
Implements hook_file_delete().
```

## Code

```php
function image_file_delete($file) {
  // Delete any image derivatives of this image.
  image_path_flush($file->uri);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
