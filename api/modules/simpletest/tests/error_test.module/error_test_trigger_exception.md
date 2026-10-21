# error_test_trigger_exception()

- **Type:** Function
- **File:** [`modules/simpletest/tests/error_test.module`](_file.md), lines 58–61 · [local source](../../../../../source/modules/simpletest/tests/error_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module#L58-L61)
- **Module/theme:** batch_test

## Signature

```php
function error_test_trigger_exception()
```

## Documentation

```text
Menu callback; trigger an exception to test the exception handler.
```

## Code

```php
function error_test_trigger_exception() {
  define('SIMPLETEST_COLLECT_ERRORS', FALSE);
  throw new Exception("Drupal is awesome");
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/error_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
