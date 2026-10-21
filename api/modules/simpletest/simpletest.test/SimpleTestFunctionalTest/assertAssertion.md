# SimpleTestFunctionalTest::assertAssertion()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 264–278 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L264-L278)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function assertAssertion($message, $type, $status, $file, $function)
```

## Documentation

```text
Assert that an assertion with the specified values is displayed
in the test results.

@param string $message Assertion message.
@param string $type Assertion type.
@param string $status Assertion status.
@param string $file File where the assertion originated.
@param string $functuion Function where the assertion originated.
@return Assertion result.
```

## Code

```php
  function assertAssertion($message, $type, $status, $file, $function) {
    $message = trim(strip_tags($message));
    $found = FALSE;
    foreach ($this->childTestResults['assertions'] as $assertion) {
      if ((strpos($assertion['message'], $message) !== FALSE) &&
          $assertion['type'] == $type &&
          $assertion['status'] == $status &&
          $assertion['file'] == $file &&
          $assertion['function'] == $function) {
        $found = TRUE;
        break;
      }
    }
    return $this->assertTrue($found, format_string('Found assertion {"@message", "@type", "@status", "@file", "@function"}.', array('@message' => $message, '@type' => $type, '@status' => $status, "@file" => $file, "@function" => $function)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
