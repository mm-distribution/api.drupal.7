# template_preprocess_overlay()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 513–518 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L513-L518)
- **Module/theme:** overlay

## Signature

```php
function template_preprocess_overlay(&$variables)
```

## Documentation

```text
Implements template_preprocess_HOOK() for overlay.tpl.php

If the current page request is inside the overlay, add appropriate classes
to the <body> element, and simplify the page title.

@see template_process_overlay()
@see overlay.tpl.php
```

## Code

```php
function template_preprocess_overlay(&$variables) {
  $variables['tabs'] = menu_primary_local_tasks();
  $variables['title'] = drupal_get_title();
  $variables['disable_overlay'] = overlay_disable_message();
  $variables['content_attributes_array']['class'][] = 'clearfix';
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
