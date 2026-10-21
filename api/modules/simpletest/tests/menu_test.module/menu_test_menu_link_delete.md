# menu_test_menu_link_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 516–518 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L516-L518)
- **Module/theme:** batch_test
- **Implements:** [hook_menu_link_delete()](../../../system/system.api.php/hook_menu_link_delete.md)

## Signature

```php
function menu_test_menu_link_delete($item)
```

## Documentation

```text
Implements hook_menu_link_delete().

@return
 A random string.
```

## Code

```php
function menu_test_menu_link_delete($item) {
  menu_test_static_variable('delete');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
