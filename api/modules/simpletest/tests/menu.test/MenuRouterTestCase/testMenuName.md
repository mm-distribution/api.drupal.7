# MenuRouterTestCase::testMenuName()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 394–410 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L394-L410)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuName()
```

## Documentation

```text
Tests for menu_name parameter for hook_menu().
```

## Code

```php
  function testMenuName() {
    $admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($admin_user);

    $sql = "SELECT menu_name FROM {menu_links} WHERE router_path = 'menu_name_test'";
    $name = db_query($sql)->fetchField();
    $this->assertEqual($name, 'original', 'Menu name is "original".');

    // Change the menu_name parameter in menu_test.module, then force a menu
    // rebuild.
    menu_test_menu_name('changed');
    menu_rebuild();

    $sql = "SELECT menu_name FROM {menu_links} WHERE router_path = 'menu_name_test'";
    $name = db_query($sql)->fetchField();
    $this->assertEqual($name, 'changed', 'Menu name was successfully changed after rebuild.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
