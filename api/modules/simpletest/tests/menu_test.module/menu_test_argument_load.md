# menu_test_argument_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 350–352 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L350-L352)
- **Module/theme:** batch_test

## Signature

```php
function menu_test_argument_load($arg1)
```

## Documentation

```text
Dummy argument loader for hook_menu() to point to.
```

## Code

```php
function menu_test_argument_load($arg1) {
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
