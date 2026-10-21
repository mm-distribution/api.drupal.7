# overlay_get_mode()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 603–605 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L603-L605)
- **Module/theme:** overlay

## Signature

```php
function overlay_get_mode()
```

## Documentation

```text
Gets the current overlay mode.

@see overlay_set_mode()
```

## Code

```php
function overlay_get_mode() {
  return overlay_set_mode(NULL);
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
