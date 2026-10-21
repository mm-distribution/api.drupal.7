# template_process_overlay()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 528–530 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L528-L530)
- **Module/theme:** overlay

## Signature

```php
function template_process_overlay(&$variables)
```

## Documentation

```text
Implements template_process_HOOK() for overlay.tpl.php

Places the rendered HTML for the page body into a top level variable.

@see template_preprocess_overlay()
@see overlay.tpl.php
```

## Code

```php
function template_process_overlay(&$variables) {
  $variables['page'] = $variables['page']['#children'];
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
