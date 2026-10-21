# system_block_view()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2105–2130 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2105-L2130)
- **Module/theme:** system
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function system_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generate a block with a promotional link to Drupal.org and
all system menu blocks.
```

## Code

```php
function system_block_view($delta = '') {
  $block = array();
  switch ($delta) {
    case 'main':
      $block['subject'] = NULL;
      $block['content'] = drupal_set_page_content();
      return $block;
    case 'powered-by':
      $block['subject'] = NULL;
      $block['content'] = theme('system_powered_by');
      return $block;
    case 'help':
      $block['subject'] = NULL;
      $block['content'] = menu_get_active_help();
      return $block;
    default:
      // All system menu blocks.
      $system_menus = menu_list_system_menus();
      if (isset($system_menus[$delta])) {
        $block['subject'] = t($system_menus[$delta]);
        $block['content'] = menu_tree($delta);
        return $block;
      }
      break;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
