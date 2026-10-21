# dashboard_enable()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.install`](_file.md), lines 49–71 · [local source](../../../../source/modules/dashboard/dashboard.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install#L49-L71)
- **Module/theme:** dashboard
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function dashboard_enable()
```

## Documentation

```text
Implements hook_enable().

Restores blocks to the dashboard that were there when the dashboard module
was disabled.
```

## Code

```php
function dashboard_enable() {
  global $theme_key;
  if (!$stashed_blocks = variable_get('dashboard_stashed_blocks')) {
    return;
  }
  if (!$admin_theme = variable_get('admin_theme')) {
    drupal_theme_initialize();
    $admin_theme = $theme_key;
  }
  foreach ($stashed_blocks as $block) {
    db_update('block')
      ->fields(array(
        'status' => 1,
        'region' => $block['region']
      ))
      ->condition('module', $block['module'])
      ->condition('delta', $block['delta'])
      ->condition('theme', $admin_theme)
      ->condition('status', 0)
      ->execute();
  }
  variable_del('dashboard_stashed_blocks');
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.install](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install) · Licensed GPL-2.0-or-later (see LICENSE)._
