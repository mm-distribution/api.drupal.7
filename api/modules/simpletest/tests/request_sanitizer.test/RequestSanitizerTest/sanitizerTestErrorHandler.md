# RequestSanitizerTest::sanitizerTestErrorHandler()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 219–221 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L219-L221)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function sanitizerTestErrorHandler($errno, $errstr)
```

## Documentation

```text
Catches and logs errors to $this->errors.

@param int $errno
  The severity level of the error.
@param string $errstr
  The error message.
```

## Code

```php
  public function sanitizerTestErrorHandler($errno, $errstr) {
    $this->errors[] = compact('errno', 'errstr');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
