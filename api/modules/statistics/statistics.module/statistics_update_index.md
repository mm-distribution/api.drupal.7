# statistics_update_index()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 460–462 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L460-L462)
- **Module/theme:** statistics
- **Implements:** [hook_update_index()](../../search/search.api.php/hook_update_index.md)

## Signature

```php
function statistics_update_index()
```

## Documentation

```text
Implements hook_update_index().
```

## Code

```php
function statistics_update_index() {
  variable_set('node_cron_views_scale', 1.0 / max(1, db_query('SELECT MAX(totalcount) FROM {node_counter}')->fetchField()));
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
