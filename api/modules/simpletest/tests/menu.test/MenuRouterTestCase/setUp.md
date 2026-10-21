# MenuRouterTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 133–141 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L133-L141)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Enable dummy module that implements hook_menu.
    parent::setUp('menu_test');
    // Make the tests below more robust by explicitly setting the default theme
    // and administrative theme that they expect.
    theme_enable(array('bartik'));
    variable_set('theme_default', 'bartik');
    variable_set('admin_theme', 'seven');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
