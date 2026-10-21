# menu_test_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 367–369 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L367-L369)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_callback()
```

## Documentation

```text
Dummy callback for hook_menu() to point to.

@return
 A random string.
```

## Code

```php
function menu_test_callback() {
  return 'This is menu_test_callback().';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
