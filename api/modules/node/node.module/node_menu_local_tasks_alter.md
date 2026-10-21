# node_menu_local_tasks_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2160–2171 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2160-L2171)
- **Module/theme:** node
- **Implements:** [hook_menu_local_tasks_alter()](../../system/system.api.php/hook_menu_local_tasks_alter.md)

## Signature

```php
function node_menu_local_tasks_alter(&$data, $router_item, $root_path)
```

## Documentation

```text
Implements hook_menu_local_tasks_alter().
```

## Code

```php
function node_menu_local_tasks_alter(&$data, $router_item, $root_path) {
  // Add action link to 'node/add' on 'admin/content' page.
  if ($root_path == 'admin/content') {
    $item = menu_get_item('node/add');
    if ($item['access']) {
      $data['actions']['output'][] = array(
        '#theme' => 'menu_local_action',
        '#link' => $item,
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
