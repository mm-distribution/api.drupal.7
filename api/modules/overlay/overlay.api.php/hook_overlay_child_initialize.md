# hook_overlay_child_initialize()

- **Type:** Hook (documentation function)
- **File:** [`modules/overlay/overlay.api.php`](_file.md), lines 33–36 · [local source](../../../../source/modules/overlay/overlay.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.api.php#L33-L36)
- **Module/theme:** overlay
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_overlay_child_initialize()
```

## Documentation

```text
Allow modules to act when an overlay child window is initialized.

The child window is initialized when a page is displayed from within the
overlay, so modules can act here if they need to take action to work from
within the confines of the overlay.
```

## Code

```php
function hook_overlay_child_initialize() {
  // Add our custom JavaScript.
  drupal_add_js(drupal_get_path('module', 'hook') . '/hook-overlay-child.js');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_overlay_child_initialize()".

- [overlay_overlay_child_initialize()](../overlay.module/overlay_overlay_child_initialize.md) — `modules/overlay/overlay.module`

---
_Drupal 7.103 · [modules/overlay/overlay.api.php](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
