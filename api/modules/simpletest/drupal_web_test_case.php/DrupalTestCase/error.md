# DrupalTestCase::error()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 486–494 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L486-L494)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function error($message = '', $group = 'Other', array $caller = NULL)
```

## Documentation

```text
Fire an error assertion.

@param $message
  The message to display along with the assertion.
@param $group
  The type of assertion - examples are "Browser", "PHP".
@param $caller
  The caller of the error.
@return
  FALSE.
```

## Code

```php
  protected function error($message = '', $group = 'Other', array $caller = NULL) {
    if ($group == 'User notice') {
      // Since 'User notice' is set by trigger_error() which is used for debug
      // set the message to a status of 'debug'.
      return $this->assert('debug', $message, 'Debug', $caller);
    }

    return $this->assert('exception', $message, $group, $caller);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
