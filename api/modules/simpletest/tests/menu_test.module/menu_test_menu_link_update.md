# menu_test_menu_link_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 506–508 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L506-L508)
- **Module/theme:** batch_test
- **Implements:** [hook_menu_link_update()](../../../system/system.api.php/hook_menu_link_update.md)

## Signature

```php
function menu_test_menu_link_update($item)
```

## Documentation

```text
Implements hook_menu_link_update().

@return
 A random string.
```

## Code

```php
function menu_test_menu_link_update($item) {
  menu_test_static_variable('update');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
