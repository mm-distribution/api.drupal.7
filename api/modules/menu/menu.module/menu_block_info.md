# menu_block_info()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 492–503 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L492-L503)
- **Module/theme:** menu
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function menu_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function menu_block_info() {
  $menus = menu_get_menus(FALSE);

  $blocks = array();
  foreach ($menus as $name => $title) {
    $blocks[$name]['info'] = check_plain($title);
    // Menu blocks can't be cached because each menu item can have
    // a custom access callback. menu.inc manages its own caching.
    $blocks[$name]['cache'] = DRUPAL_NO_CACHE;
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
