# system_test_page_shutdown_functions()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 435–437 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L435-L437)
- **Module/theme:** batch_test

## Signature

```php
function system_test_page_shutdown_functions($arg1, $arg2)
```

## Documentation

```text
A simple page callback which adds a register shutdown function.
```

## Code

```php
function system_test_page_shutdown_functions($arg1, $arg2) {
  drupal_register_shutdown_function('_system_test_first_shutdown_function', $arg1, $arg2);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
