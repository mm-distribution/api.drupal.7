# DrupalTestCase::errorHandler()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 595–622 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L595-L622)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public function errorHandler($severity, $message, $file = NULL, $line = NULL)
```

## Documentation

```text
Handle errors during test runs.

Because this is registered in set_error_handler(), it has to be public.
@see set_error_handler
```

## Code

```php
  public function errorHandler($severity, $message, $file = NULL, $line = NULL) {
    if ($severity & error_reporting()) {
      $error_map = array(
        E_STRICT => 'Run-time notice',
        E_WARNING => 'Warning',
        E_NOTICE => 'Notice',
        E_CORE_ERROR => 'Core error',
        E_CORE_WARNING => 'Core warning',
        E_USER_ERROR => 'User error',
        E_USER_WARNING => 'User warning',
        E_USER_NOTICE => 'User notice',
        E_RECOVERABLE_ERROR => 'Recoverable error',
      );

      // PHP 5.3 adds new error logging constants. Add these conditionally for
      // backwards compatibility with PHP 5.2.
      if (defined('E_DEPRECATED')) {
        $error_map += array(
          E_DEPRECATED => 'Deprecated',
          E_USER_DEPRECATED => 'User deprecated',
        );
      }

      $backtrace = debug_backtrace();
      $this->error($message, $error_map[$severity], _drupal_get_last_caller($backtrace));
    }
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
