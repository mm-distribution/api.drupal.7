# menu_node_prepare()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 589–634 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L589-L634)
- **Module/theme:** menu
- **Implements:** [hook_node_prepare()](../../node/node.api.php/hook_node_prepare.md)

## Signature

```php
function menu_node_prepare($node)
```

## Documentation

```text
Implements hook_node_prepare().
```

## Code

```php
function menu_node_prepare($node) {
  if (empty($node->menu)) {
    // Prepare the node for the edit form so that $node->menu always exists.
    $menu_name = strtok(variable_get('menu_parent_' . $node->type, 'main-menu:0'), ':');
    $item = array();
    if (isset($node->nid)) {
      $mlid = FALSE;
      // Give priority to the default menu
      $type_menus = variable_get('menu_options_' . $node->type, array('main-menu' => 'main-menu'));
      if (in_array($menu_name, $type_menus)) {
        $mlid = db_query_range("SELECT mlid FROM {menu_links} WHERE link_path = :path AND menu_name = :menu_name AND module = 'menu' ORDER BY mlid ASC", 0, 1, array(
          ':path' => 'node/' . $node->nid,
          ':menu_name' => $menu_name,
        ))->fetchField();
      }
      // Check all allowed menus if a link does not exist in the default menu.
      if (!$mlid && !empty($type_menus)) {
        $mlid = db_query_range("SELECT mlid FROM {menu_links} WHERE link_path = :path AND module = 'menu' AND menu_name IN (:type_menus) ORDER BY mlid ASC", 0, 1, array(
          ':path' => 'node/' . $node->nid,
          ':type_menus' => array_values($type_menus),
        ))->fetchField();
      }
      if ($mlid) {
        $item = menu_link_load($mlid);
      }
    }
    // Set default values.
    $node->menu = $item + array(
      'link_title' => '',
      'mlid' => 0,
      'plid' => 0,
      'menu_name' => $menu_name,
      'weight' => 0,
      'options' => array(),
      'module' => 'menu',
      'expanded' => 0,
      'hidden' => 0,
      'has_children' => 0,
      'customized' => 0,
    );
  }
  // Find the depth limit for the parent select.
  if (!isset($node->menu['parent_depth_limit'])) {
    $node->menu['parent_depth_limit'] = _menu_parent_depth_limit($node->menu);
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
