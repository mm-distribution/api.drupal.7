# node_access_test_menu()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 80–95 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L80-L95)
- **Module/theme:** node_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function node_access_test_menu()
```

## Documentation

```text
Implements hook_menu().

Sets up a page that lists nodes.
```

## Code

```php
function node_access_test_menu() {
  $items = array();
  $items['node_access_test_page'] = array(
    'title' => 'Node access test',
    'page callback' => 'node_access_test_page',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
  );
  $items['node_access_entity_test_page'] = array(
    'title' => 'Node access test',
    'page callback' => 'node_access_entity_test_page',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
