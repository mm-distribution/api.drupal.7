# DrupalTestCase::exceptionHandler()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 629–639 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L629-L639)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function exceptionHandler($exception)
```

## Documentation

```text
Handle exceptions.

@see set_exception_handler
```

## Code

```php
  protected function exceptionHandler($exception) {
    $backtrace = $exception->getTrace();
    // Push on top of the backtrace the call that generated the exception.
    array_unshift($backtrace, array(
      'line' => $exception->getLine(),
      'file' => $exception->getFile(),
    ));
    require_once DRUPAL_ROOT . '/includes/errors.inc';
    // The exception message is run through check_plain() by _drupal_decode_exception().
    $this->error(t('%type: !message in %function (line %line of %file).', _drupal_decode_exception($exception)), 'Uncaught exception', _drupal_get_last_caller($backtrace));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
