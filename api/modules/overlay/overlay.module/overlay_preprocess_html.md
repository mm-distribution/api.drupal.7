# overlay_preprocess_html()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 485–490 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L485-L490)
- **Module/theme:** overlay

## Signature

```php
function overlay_preprocess_html(&$variables)
```

## Documentation

```text
Implements hook_preprocess_html().

If the current page request is inside the overlay, add appropriate classes
to the <body> element, and simplify the page title.

@see overlay_get_mode()
```

## Code

```php
function overlay_preprocess_html(&$variables) {
  if (overlay_get_mode() == 'child') {
    // Add overlay class, so themes can react to being displayed in the overlay.
    $variables['classes_array'][] = 'overlay';
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
