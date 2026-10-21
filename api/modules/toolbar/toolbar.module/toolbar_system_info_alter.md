# toolbar_system_info_alter()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 177–181 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L177-L181)
- **Module/theme:** toolbar
- **Implements:** [hook_system_info_alter()](../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function toolbar_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Indicate that the 'page_top' region (in which the toolbar will be displayed)
is an overlay supplemental region that should be refreshed whenever its
content is updated.

This information is provided for any module that might need to use it, not
just the core Overlay module.
```

## Code

```php
function toolbar_system_info_alter(&$info, $file, $type) {
  if ($type == 'theme') {
    $info['overlay_supplemental_regions'][] = 'page_top';
  }
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
