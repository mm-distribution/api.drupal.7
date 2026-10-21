# dashboard_update()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 543–582 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L543-L582)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_update()
```

## Documentation

```text
Sets the new weight of each region according to the drag-and-drop order.
```

## Code

```php
function dashboard_update() {
  drupal_theme_initialize();
  global $theme_key;
  // Check the form token to make sure we have a valid request.
  if (!empty($_REQUEST['form_token']) && drupal_valid_token($_REQUEST['form_token'], 'dashboard-update')) {
    parse_str($_REQUEST['regions'], $regions);
    foreach ($regions as $region_name => $blocks) {
      if ($region_name == 'disabled_blocks') {
        $region_name = 'dashboard_inactive';
      }
      foreach ($blocks as $weight => $block_string) {
        // Parse the query string to determine the block's module and delta.
        preg_match('/block-([^-]+)-(.+)/', $block_string, $matches);
        $block = new stdClass();
        $block->module = $matches[1];
        $block->delta = $matches[2];

        $block->region = $region_name;
        $block->weight = $weight;
        $block->status = 1;

        db_merge('block')
          ->key(array(
            'module' => $block->module,
            'delta' => $block->delta,
            'theme' => $theme_key,
          ))
          ->fields(array(
            'status' => $block->status,
            'weight' => $block->weight,
            'region' => $block->region,
            'pages' => '',
          ))
          ->execute();
      }
    }
    drupal_set_message(t('The configuration options have been saved.'), 'status', FALSE);
  }
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
