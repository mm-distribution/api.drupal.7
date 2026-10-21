# overlay_preprocess_maintenance_page()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 500–502 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L500-L502)
- **Module/theme:** overlay

## Signature

```php
function overlay_preprocess_maintenance_page(&$variables)
```

## Documentation

```text
Implements hook_preprocess_maintenance_page().

If the current page request is inside the overlay, add appropriate classes
to the <body> element, and simplify the page title.

@see overlay_preprocess_maintenance_page()
```

## Code

```php
function overlay_preprocess_maintenance_page(&$variables) {
  overlay_preprocess_html($variables);
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
