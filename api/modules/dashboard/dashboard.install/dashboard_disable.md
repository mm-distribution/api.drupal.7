# dashboard_disable()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.install`](_file.md), lines 15–41 · [local source](../../../../source/modules/dashboard/dashboard.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install#L15-L41)
- **Module/theme:** dashboard
- **Implements:** [hook_disable()](../../system/system.api.php/hook_disable.md)

## Signature

```php
function dashboard_disable()
```

## Documentation

```text
Implements hook_disable().

Stash a list of blocks enabled on the dashboard, so they can be re-enabled
if the dashboard is re-enabled. Then disable those blocks, since the
dashboard regions will no longer be defined.
```

## Code

```php
function dashboard_disable() {
  // Stash a list of currently enabled blocks.
  $stashed_blocks = array();

  $result = db_select('block', 'b')
    ->fields('b', array('module', 'delta', 'region'))
    ->condition('b.region', dashboard_regions(), 'IN')
    ->execute();

  foreach ($result as $block) {
    $stashed_blocks[] = array(
      'module' => $block->module,
      'delta' => $block->delta,
      'region' => $block->region,
    );
  }
  variable_set('dashboard_stashed_blocks', $stashed_blocks);

  // Disable the dashboard blocks.
  db_update('block')
    ->fields(array(
      'status' => 0,
      'region' => BLOCK_REGION_NONE,
    ))
    ->condition('region', dashboard_regions(), 'IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.install](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install) · Licensed GPL-2.0-or-later (see LICENSE)._
