# dashboard_show_disabled()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 494–510 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L494-L510)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_show_disabled()
```

## Documentation

```text
Ajax callback: Shows disabled blocks in the dashboard customization mode.
```

## Code

```php
function dashboard_show_disabled() {
  global $theme_key;

  // Blocks are not necessarily initialized at this point.
  $blocks = _block_rehash();

  // Limit the list to blocks that are marked as disabled for the dashboard.
  foreach ($blocks as $key => $block) {
    if ($block['theme'] != $theme_key || $block['region'] != 'dashboard_inactive') {
      unset($blocks[$key]);
    }
  }

  // Theme the output and end the page request.
  print theme('dashboard_disabled_blocks', array('blocks' => $blocks));
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
