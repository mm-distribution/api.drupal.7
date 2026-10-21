# JavaScriptTestCase::testNoCache()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1815–1818 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1815-L1818)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNoCache()
```

## Documentation

```text
Test drupal_add_js() sets preproccess to false when cache is set to false.
```

## Code

```php
  function testNoCache() {
    $javascript = drupal_add_js('misc/collapse.js', array('cache' => FALSE));
    $this->assertFalse($javascript['misc/collapse.js']['preprocess'], 'Setting cache to FALSE sets proprocess to FALSE when adding JavaScript.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
