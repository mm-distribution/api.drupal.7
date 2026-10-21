# FileHookTestCase::assertFileHookCalled()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 288–303 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L288-L303)
- **Class:** [FileHookTestCase](../FileHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertFileHookCalled($hook, $expected_count = 1, $message = NULL)
```

## Documentation

```text
Assert that a hook_file_* hook was called a certain number of times.

@param $hook
  String with the hook name, e.g. 'load', 'save', 'insert', etc.
@param $expected_count
  Optional integer count.
@param $message
  Optional translated string message.
```

## Code

```php
  function assertFileHookCalled($hook, $expected_count = 1, $message = NULL) {
    $actual_count = count(file_test_get_calls($hook));

    if (!isset($message)) {
      if ($actual_count == $expected_count) {
        $message = format_string('hook_file_@name was called correctly.', array('@name' => $hook));
      }
      elseif ($expected_count == 0) {
        $message = format_plural($actual_count, 'hook_file_@name was not expected to be called but was actually called once.', 'hook_file_@name was not expected to be called but was actually called @count times.', array('@name' => $hook, '@count' => $actual_count));
      }
      else {
        $message = format_string('hook_file_@name was expected to be called %expected times but was called %actual times.', array('@name' => $hook, '%expected' => $expected_count, '%actual' => $actual_count));
      }
    }
    $this->assertEqual($actual_count, $expected_count, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
