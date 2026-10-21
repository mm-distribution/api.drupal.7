# MenuRouterTestCase::testMenuItemHooks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 541–551 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L541-L551)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuItemHooks()
```

## Documentation

```text
Test menu maintenance hooks.
```

## Code

```php
  function testMenuItemHooks() {
    // Create an item.
    menu_link_maintain('menu_test', 'insert', 'menu_test_maintain/4', 'Menu link #4');
    $this->assertEqual(menu_test_static_variable(), 'insert', 'hook_menu_link_insert() fired correctly');
    // Update the item.
    menu_link_maintain('menu_test', 'update', 'menu_test_maintain/4', 'Menu link updated');
    $this->assertEqual(menu_test_static_variable(), 'update', 'hook_menu_link_update() fired correctly');
    // Delete the item.
    menu_link_maintain('menu_test', 'delete', 'menu_test_maintain/4', '');
    $this->assertEqual(menu_test_static_variable(), 'delete', 'hook_menu_link_delete() fired correctly');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
