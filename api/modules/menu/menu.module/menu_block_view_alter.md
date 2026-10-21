# menu_block_view_alter()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 522–530 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L522-L530)
- **Module/theme:** menu
- **Implements:** [hook_block_view_alter()](../../block/block.api.php/hook_block_view_alter.md)

## Signature

```php
function menu_block_view_alter(&$data, $block)
```

## Documentation

```text
Implements hook_block_view_alter().
```

## Code

```php
function menu_block_view_alter(&$data, $block) {
  // Add contextual links for system menu blocks.
  if ($block->module == 'system' && !empty($data['content'])) {
    $system_menus = menu_list_system_menus();
    if (isset($system_menus[$block->delta])) {
      $data['content']['#contextual_links']['menu'] = array('admin/structure/menu/manage', array($block->delta));
    }
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
