# overlay_enable()

- **Type:** Function
- **File:** [`modules/overlay/overlay.install`](_file.md), lines 14–19 · [local source](../../../../source/modules/overlay/overlay.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.install#L14-L19)
- **Module/theme:** overlay
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function overlay_enable()
```

## Documentation

```text
Implements hook_enable().

If the module is being enabled through the admin UI, and not from an
installation profile, reopen the modules page in an overlay.
```

## Code

```php
function overlay_enable() {
  if (strpos(current_path(), 'admin/modules') === 0) {
    // Flag for a redirect to <front>#overlay=admin/modules on hook_init().
    $_SESSION['overlay_enable_redirect'] = 1;
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.install](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.install) · Licensed GPL-2.0-or-later (see LICENSE)._
