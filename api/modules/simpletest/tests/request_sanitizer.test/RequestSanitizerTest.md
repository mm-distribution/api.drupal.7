# RequestSanitizerTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](_file.md), lines 11–272 · [local source](../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L11-L272)
- **Module/theme:** batch_test

## Signature

```php
class RequestSanitizerTest extends DrupalUnitTestCase
```

## Documentation

```text
Tests DrupalRequestSanitizer class.
```

## Properties

### $errors

```php
protected $errors;
```

```text
Log of errors triggered during sanitization.

@var array
```

## Methods (derived index)

- [getInfo()](RequestSanitizerTest/getInfo.md) — {@inheritdoc}
- [setUp()](RequestSanitizerTest/setUp.md) — {@inheritdoc}
- [testRequestSanitization()](RequestSanitizerTest/testRequestSanitization.md) — Iterate through all the RequestSanitizerTests.
- [requestSanitizationTest()](RequestSanitizerTest/requestSanitizationTest.md) — Tests RequestSanitizer class.
- [requestSanitizerTests()](RequestSanitizerTest/requestSanitizerTests.md) — Data provider for testRequestSanitization.
- [sanitizerTestErrorHandler()](RequestSanitizerTest/sanitizerTestErrorHandler.md) — Catches and logs errors to $this->errors.
- [assertError()](RequestSanitizerTest/assertError.md) — Asserts that the expected error has been logged.
- [assertEqualLabelled()](RequestSanitizerTest/assertEqualLabelled.md) — Asserts two values are equal, includes a label.

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
