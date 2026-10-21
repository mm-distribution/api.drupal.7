# RequestSanitizerTest::testRequestSanitization()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 43–55 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L43-L55)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testRequestSanitization()
```

## Documentation

```text
Iterate through all the RequestSanitizerTests.
```

## Code

```php
  public function testRequestSanitization() {
    foreach ($this->requestSanitizerTests() as $label => $data) {
      $this->errors = array();
      // Normalize the test parameters.
      $test = array(
        'request' => $data[0],
        'expected' => isset($data[1]) ? $data[1] : array(),
        'expected_errors' => isset($data[2]) ? $data[2] : NULL,
        'whitelist' => isset($data[3]) ? $data[3] : array(),
      );
      $this->requestSanitizationTest($test['request'], $test['expected'], $test['expected_errors'], $test['whitelist'], $label);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
