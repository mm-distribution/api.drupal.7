# JavaScriptTestCase::testDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1557–1559 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1557-L1559)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDefault()
```

## Documentation

```text
Test default JavaScript is empty.
```

## Code

```php
  function testDefault() {
    $this->assertEqual(array(), drupal_add_js(), 'Default JavaScript is empty.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
