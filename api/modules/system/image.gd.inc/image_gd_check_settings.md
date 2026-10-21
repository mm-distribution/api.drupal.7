# image_gd_check_settings()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 58–61 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L58-L61)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_check_settings()
```

## Documentation

```text
Verify GD2 settings (that the right version is actually installed).

@return
  A boolean indicating if the GD toolkit is available on this machine.
```

## Code

```php
function image_gd_check_settings() {
  // GD2 support is available.
  return function_exists('imagegd2');
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
