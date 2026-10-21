# hook_overlay_parent_initialize()

- **Type:** Hook (documentation function)
- **File:** [`modules/overlay/overlay.api.php`](_file.md), lines 21–24 · [local source](../../../../source/modules/overlay/overlay.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.api.php#L21-L24)
- **Module/theme:** overlay
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_overlay_parent_initialize()
```

## Documentation

```text
Allow modules to act when an overlay parent window is initialized.

The parent window is initialized when a page is displayed in which the
overlay might be required to be displayed, so modules can act here if they
need to take action to accommodate the possibility of the overlay appearing
within a Drupal page.
```

## Code

```php
function hook_overlay_parent_initialize() {
  // Add our custom JavaScript.
  drupal_add_js(drupal_get_path('module', 'hook') . '/hook-overlay.js');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_overlay_parent_initialize()".

- [overlay_overlay_parent_initialize()](../overlay.module/overlay_overlay_parent_initialize.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/overlay/overlay.api.php](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
