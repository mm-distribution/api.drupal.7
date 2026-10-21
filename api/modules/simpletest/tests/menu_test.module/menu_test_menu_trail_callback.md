# menu_test_menu_trail_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 374–380 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L374-L380)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_menu_trail_callback()
```

## Documentation

```text
Callback that test menu_test_menu_tree_set_path().
```

## Code

```php
function menu_test_menu_trail_callback() {
  $menu_path = variable_get('menu_test_menu_tree_set_path', array());
  if (!empty($menu_path)) {
    menu_tree_set_path($menu_path['menu_name'], $menu_path['path']);
  }
  return 'This is menu_test_menu_trail_callback().';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
