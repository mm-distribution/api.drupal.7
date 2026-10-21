# RequestSanitizerTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 34–38 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L34-L38)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function setUp()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  protected function setUp() {
    require_once DRUPAL_ROOT . '/includes/request-sanitizer.inc';
    parent::setUp();
    set_error_handler(array($this, "sanitizerTestErrorHandler"));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
