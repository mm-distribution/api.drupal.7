# RequestSanitizerTest::assertError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 236–244 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L236-L244)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertError($errstr, $errno, $label)
```

## Documentation

```text
Asserts that the expected error has been logged.

@param string $errstr
  The error message.
@param int $errno
  The severity level of the error.
@param string $label
  The label to include with the message.

@return bool
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertError($errstr, $errno, $label) {
    $label = (empty($label)) ? '' : $label . ': ';
    foreach ($this->errors as $error) {
      if ($error['errstr'] === $errstr && $error['errno'] === $errno) {
        return $this->pass($label . "Error with level $errno and message '$errstr' found");
      }
    }
    return $this->fail($label . "Error with level $errno and message '$errstr' not found in " . var_export($this->errors, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
