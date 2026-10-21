# DrupalTestCase::assert()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 165–205 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L165-L205)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assert($status, $message = '', $group = 'Other', array $caller = NULL)
```

## Documentation

```text
Internal helper: stores the assert.

@param $status
  Can be 'pass', 'fail', 'exception'.
  TRUE is a synonym for 'pass', FALSE for 'fail'.
@param $message
  The message string.
@param $group
  Which group this assert belongs to.
@param $caller
  By default, the assert comes from a function whose name starts with
  'test'. Instead, you can specify where this assert originates from
  by passing in an associative array as $caller. Key 'file' is
  the name of the source file, 'line' is the line number and 'function'
  is the caller function itself.
```

## Code

```php
  protected function assert($status, $message = '', $group = 'Other', array $caller = NULL) {
    // Convert boolean status to string status.
    if (is_bool($status)) {
      $status = $status ? 'pass' : 'fail';
    }

    // Increment summary result counter.
    $this->results['#' . $status]++;

    // Get the function information about the call to the assertion method.
    if (!$caller) {
      $caller = $this->getAssertionCall();
    }

    // Creation assertion array that can be displayed while tests are running.
    $this->assertions[] = $assertion = array(
      'test_id' => $this->testId,
      'test_class' => get_class($this),
      'status' => $status,
      'message' => $message,
      'message_group' => $group,
      'function' => $caller['function'],
      'line' => $caller['line'],
      'file' => $caller['file'],
    );

    // Store assertion for display after the test has completed.
    self::getDatabaseConnection()
      ->insert('simpletest')
      ->fields($assertion)
      ->execute();

    // We do not use a ternary operator here to allow a breakpoint on
    // test failure.
    if ($status == 'pass') {
      return TRUE;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
