# image_install()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 11–15 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L11-L15)
- **Module/theme:** image
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function image_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function image_install() {
  // Create the styles directory and ensure it's writable.
  $directory = file_default_scheme() . '://styles';
  file_prepare_directory($directory, FILE_CREATE_DIRECTORY | FILE_MODIFY_PERMISSIONS);
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
