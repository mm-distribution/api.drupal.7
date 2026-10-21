# system_page_alter()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3564–3573 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3564-L3573)
- **Module/theme:** system
- **Implements:** [hook_page_alter()](../system.api.php/hook_page_alter.md)

## Signature

```php
function system_page_alter(&$page)
```

## Documentation

```text
Implements hook_page_alter().
```

## Code

```php
function system_page_alter(&$page) {
  // Find all non-empty page regions, and add a theme wrapper function that
  // allows them to be consistently themed.
  foreach (system_region_list($GLOBALS['theme'], REGIONS_ALL, FALSE) as $region) {
    if (!empty($page[$region])) {
      $page[$region]['#theme_wrappers'][] = 'region';
      $page[$region]['#region'] = $region;
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
