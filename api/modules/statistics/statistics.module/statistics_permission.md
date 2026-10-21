# statistics_permission()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 98–110 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L98-L110)
- **Module/theme:** statistics
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function statistics_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function statistics_permission() {
  return array(
    'administer statistics' => array(
      'title' => t('Administer statistics'),
    ),
    'access statistics' => array(
      'title' => t('View content access statistics'),
    ),
    'view post access counter' => array(
      'title' => t('View content hits'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
