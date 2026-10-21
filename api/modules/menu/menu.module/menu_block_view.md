# menu_block_view()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 508–517 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L508-L517)
- **Module/theme:** menu
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function menu_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function menu_block_view($delta = '') {
  $menus = menu_get_menus(FALSE);
  $data['subject'] = check_plain($menus[$delta]);
  $data['content'] = menu_tree($delta);
  // Add contextual links for this block.
  if (!empty($data['content'])) {
    $data['content']['#contextual_links']['menu'] = array('admin/structure/menu/manage', array($delta));
  }
  return $data;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
