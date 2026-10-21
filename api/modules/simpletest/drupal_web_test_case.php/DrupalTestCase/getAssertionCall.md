# DrupalTestCase::getAssertionCall()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 294–308 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L294-L308)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function getAssertionCall()
```

## Documentation

```text
Cycles through backtrace until the first non-assertion method is found.

@return
  Array representing the true caller.
```

## Code

```php
  protected function getAssertionCall() {
    $backtrace = debug_backtrace();

    // The first element is the call. The second element is the caller.
    // We skip calls that occurred in one of the methods of our base classes
    // or in an assertion function.
   while (($caller = $backtrace[1]) &&
         ((isset($caller['class']) && isset($this->skipClasses[$caller['class']])) ||
           substr($caller['function'], 0, 6) == 'assert')) {
      // We remove that call.
      array_shift($backtrace);
    }

    return _drupal_get_last_caller($backtrace);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
