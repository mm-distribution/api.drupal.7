# error_test_generate_warnings()

- **Type:** Function
- **File:** [`modules/simpletest/tests/error_test.module`](_file.md), lines 39–53 · [local source](../../../../../source/modules/simpletest/tests/error_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module#L39-L53)
- **Module/theme:** batch_test

## Signature

```php
function error_test_generate_warnings($collect_errors = FALSE)
```

## Documentation

```text
Menu callback; generate warnings to test the error handler.
```

## Code

```php
function error_test_generate_warnings($collect_errors = FALSE) {
  // Tell Drupal error reporter to send errors to Simpletest or not.
  define('SIMPLETEST_COLLECT_ERRORS', $collect_errors);
  // This will generate a notice.
  $notice = new \stdClass();
  $notice == 1 ? 1 : 0;
  // This will generate a warning.
  $a = '';
  foreach ($a as $b) {

  }
  // This will generate a user error.
  trigger_error("Drupal is awesome", E_USER_WARNING);
  return "";
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/error_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
