# menu_test_menu_link_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 496–498 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L496-L498)
- **Module/theme:** batch_test
- **Implements:** [hook_menu_link_insert()](../../../system/system.api.php/hook_menu_link_insert.md)

## Signature

```php
function menu_test_menu_link_insert($item)
```

## Documentation

```text
Implements hook_menu_link_insert().

@return
 A random string.
```

## Code

```php
function menu_test_menu_link_insert($item) {
  menu_test_static_variable('insert');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
