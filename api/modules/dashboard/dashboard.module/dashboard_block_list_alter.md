# dashboard_block_list_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 124–132 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L124-L132)
- **Module/theme:** dashboard
- **Implements:** [hook_block_list_alter()](../../block/block.api.php/hook_block_list_alter.md)

## Signature

```php
function dashboard_block_list_alter(&$blocks)
```

## Documentation

```text
Implements hook_block_list_alter().

Skip rendering dashboard blocks when not on the dashboard page itself. This
prevents expensive dashboard blocks from causing performance issues on pages
where they will never be displayed.
```

## Code

```php
function dashboard_block_list_alter(&$blocks) {
  if (!dashboard_is_visible()) {
    foreach ($blocks as $key => $block) {
      if (in_array($block->region, dashboard_regions())) {
        unset($blocks[$key]);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
