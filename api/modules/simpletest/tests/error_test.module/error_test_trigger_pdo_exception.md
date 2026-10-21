# error_test_trigger_pdo_exception()

- **Type:** Function
- **File:** [`modules/simpletest/tests/error_test.module`](_file.md), lines 66–69 · [local source](../../../../../source/modules/simpletest/tests/error_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module#L66-L69)
- **Module/theme:** batch_test

## Signature

```php
function error_test_trigger_pdo_exception()
```

## Documentation

```text
Menu callback; trigger an exception to test the exception handler.
```

## Code

```php
function error_test_trigger_pdo_exception() {
  define('SIMPLETEST_COLLECT_ERRORS', FALSE);
  db_query('SELECT * FROM bananas_are_awesome');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/error_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
