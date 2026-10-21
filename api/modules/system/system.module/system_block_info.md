# system_block_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2066–2097 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2066-L2097)
- **Module/theme:** system
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function system_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function system_block_info() {
  $blocks['main'] = array(
    'info' => t('Main page content'),
     // Cached elsewhere.
    'cache' => DRUPAL_NO_CACHE,
    // Auto-enable in 'content' region by default, which always exists.
    // @see system_themes_page(), drupal_render_page()
    'status' => 1,
    'region' => 'content',
  );
  $blocks['powered-by'] = array(
    'info' => t('Powered by Drupal'),
    'weight' => '10',
    'cache' => DRUPAL_NO_CACHE,
  );
  $blocks['help'] = array(
    'info' => t('System help'),
    'weight' => '5',
    'cache' => DRUPAL_NO_CACHE,
    // Auto-enable in 'help' region by default, if the theme defines one.
    'status' => 1,
    'region' => 'help',
  );
  // System-defined menu blocks.
  foreach (menu_list_system_menus() as $menu_name => $title) {
    $blocks[$menu_name]['info'] = t($title);
    // Menu blocks can't be cached because each menu item can have
    // a custom access callback. menu.inc manages its own caching.
    $blocks[$menu_name]['cache'] = DRUPAL_NO_CACHE;
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
