# MenuRouterTestCase::testMenuGetNames()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 369–389 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L369-L389)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuGetNames()
```

## Documentation

```text
Test menu_get_names().
```

## Code

```php
  function testMenuGetNames() {
    // Create three menu items.
    for ($i = 0; $i < 3; $i++) {
      $menu_link = array(
        'link_title' => 'Menu link #' . $i,
        'link_path' => 'menu_test/' . $i,
        'module' => 'menu_test',
        'menu_name' => 'menu_test_' . $i,
      );
      menu_link_save($menu_link);
    }

    drupal_static_reset('menu_get_names');

    // Verify that the menu names are correctly reported by menu_get_names().
    $menu_names = menu_get_names();
    $this->pass(implode(' | ', $menu_names));
    for ($i = 0; $i < 3; $i++) {
      $this->assertTrue(in_array('menu_test_' . $i, $menu_names), t('Expected menu name %expected is returned.', array('%expected' => 'menu_test_' . $i)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
