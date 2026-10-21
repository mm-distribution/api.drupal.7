# JavaScriptTestCase::testReset()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1630–1634 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1630-L1634)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testReset()
```

## Documentation

```text
Test to see if resetting the JavaScript empties the cache.
```

## Code

```php
  function testReset() {
    drupal_add_js('misc/collapse.js');
    drupal_static_reset('drupal_add_js');
    $this->assertEqual(array(), drupal_add_js(), 'Resetting the JavaScript correctly empties the cache.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
