# overlay_admin_paths()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 44–52 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L44-L52)
- **Module/theme:** overlay
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function overlay_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function overlay_admin_paths() {
  $paths = array(
    // This is marked as an administrative path so that if it is visited from
    // within the overlay, the user will stay within the overlay while the
    // callback is being processed.
    'overlay/dismiss-message' => TRUE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
