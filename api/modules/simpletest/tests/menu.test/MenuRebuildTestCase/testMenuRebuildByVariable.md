# MenuRebuildTestCase::testMenuRebuildByVariable()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 905–924 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L905-L924)
- **Class:** [MenuRebuildTestCase](../MenuRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuRebuildByVariable()
```

## Documentation

```text
Test if the 'menu_rebuild_needed' variable triggers a menu_rebuild() call.
```

## Code

```php
  function testMenuRebuildByVariable() {
    // Check if 'admin' path exists.
    $admin_exists = db_query('SELECT path from {menu_router} WHERE path = :path', array(':path' => 'admin'))->fetchField();
    $this->assertEqual($admin_exists, 'admin', "The path 'admin/' exists prior to deleting.");

    // Delete the path item 'admin', and test that the path doesn't exist in the database.
    $delete = db_delete('menu_router')
      ->condition('path', 'admin')
      ->execute();
    $admin_exists = db_query('SELECT path from {menu_router} WHERE path = :path', array(':path' => 'admin'))->fetchField();
    $this->assertFalse($admin_exists, "The path 'admin/' has been deleted and doesn't exist in the database.");

    // Now we enable the rebuild variable and trigger menu_execute_active_handler()
    // to rebuild the menu item. Now 'admin' should exist.
    variable_set('menu_rebuild_needed', TRUE);
    // menu_execute_active_handler() should trigger the rebuild.
    $this->drupalGet('<front>');
    $admin_exists = db_query('SELECT path from {menu_router} WHERE path = :path', array(':path' => 'admin'))->fetchField();
    $this->assertEqual($admin_exists, 'admin', "The menu has been rebuilt, the path 'admin' now exists again.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
