# MenuRouterTestCase::testMenuLoadArgumentsInheritance()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 622–668 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L622-L668)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuLoadArgumentsInheritance()
```

## Documentation

```text
Tests inheritance of 'load arguments'.
```

## Code

```php
  function testMenuLoadArgumentsInheritance() {
    $expected = array(
      'menu-test/arguments/%/%' => array(
        2 => array('menu_test_argument_load' => array(3)),
        3 => NULL,
      ),
      // Arguments are inherited to normal children.
      'menu-test/arguments/%/%/default' => array(
        2 => array('menu_test_argument_load' => array(3)),
        3 => NULL,
      ),
      // Arguments are inherited to tab children.
      'menu-test/arguments/%/%/task' => array(
        2 => array('menu_test_argument_load' => array(3)),
        3 => NULL,
      ),
      // Arguments are only inherited to the same loader functions.
      'menu-test/arguments/%/%/common-loader' => array(
        2 => array('menu_test_argument_load' => array(3)),
        3 => 'menu_test_other_argument_load',
      ),
      // Arguments are not inherited to children not using the same loader
      // function.
      'menu-test/arguments/%/%/different-loaders-1' => array(
        2 => NULL,
        3 => 'menu_test_argument_load',
      ),
      'menu-test/arguments/%/%/different-loaders-2' => array(
        2 => 'menu_test_other_argument_load',
        3 => NULL,
      ),
      'menu-test/arguments/%/%/different-loaders-3' => array(
        2 => NULL,
        3 => NULL,
      ),
      // Explicit loader arguments should not be overriden by parent.
      'menu-test/arguments/%/%/explicit-arguments' => array(
        2 => array('menu_test_argument_load' => array()),
        3 => NULL,
      ),
    );

    foreach ($expected as $router_path => $load_functions) {
      $router_item = $this->menuLoadRouter($router_path);
      $this->assertIdentical(unserialize($router_item['load_functions']), $load_functions, format_string('Expected load functions for router %router_path' , array('%router_path' => $router_path)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
