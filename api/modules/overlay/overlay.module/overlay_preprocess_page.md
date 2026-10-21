# overlay_preprocess_page()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 539–543 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L539-L543)
- **Module/theme:** overlay

## Signature

```php
function overlay_preprocess_page(&$variables)
```

## Documentation

```text
Implements hook_preprocess_page().

If the current page request is inside the overlay, hide the tabs.

@see overlay_get_mode()
```

## Code

```php
function overlay_preprocess_page(&$variables) {
  if (overlay_get_mode() == 'child') {
    unset($variables['tabs']['#primary']);
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
