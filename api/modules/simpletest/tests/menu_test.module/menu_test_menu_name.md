# menu_test_menu_name()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 482–488 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L482-L488)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_menu_name($new_name = '')
```

## Documentation

```text
Helper function for the testMenuName() test. Used to change the menu_name
parameter of a menu.

@param $new_name
  If set, will change the menu_name value.
@return
  The menu_name value to use.
```

## Code

```php
function menu_test_menu_name($new_name = '') {
  static $name = 'original';
  if ($new_name) {
    $name = $new_name;
  }
  return $name;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
