# overlay_system_info_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 470–475 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L470-L475)
- **Module/theme:** overlay
- **Implements:** [hook_system_info_alter()](../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function overlay_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Add default regions for the overlay.
```

## Code

```php
function overlay_system_info_alter(&$info, $file, $type) {
  if ($type == 'theme') {
    $info['overlay_regions'][] = 'content';
    $info['overlay_regions'][] = 'help';
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
