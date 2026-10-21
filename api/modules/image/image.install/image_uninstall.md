# image_uninstall()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 20–23 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L20-L23)
- **Module/theme:** image
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function image_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function image_uninstall() {
  // Remove the styles directory and generated images.
  file_unmanaged_delete_recursive(file_default_scheme() . '://styles');
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
