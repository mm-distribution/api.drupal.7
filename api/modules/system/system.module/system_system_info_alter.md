# system_system_info_alter()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2778–2785 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2778-L2785)
- **Module/theme:** system
- **Implements:** [hook_system_info_alter()](../system.api.php/hook_system_info_alter.md)

## Signature

```php
function system_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().
```

## Code

```php
function system_system_info_alter(&$info, $file, $type) {
  // Remove page-top and page-bottom from the blocks UI since they are reserved for
  // modules to populate from outside the blocks system.
  if ($type == 'theme') {
    $info['regions_hidden'][] = 'page_top';
    $info['regions_hidden'][] = 'page_bottom';
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
