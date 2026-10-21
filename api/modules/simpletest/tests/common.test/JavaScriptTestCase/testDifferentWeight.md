# JavaScriptTestCase::testDifferentWeight()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1831–1834 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1831-L1834)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDifferentWeight()
```

## Documentation

```text
Test adding a JavaScript file with a different weight.
```

## Code

```php
  function testDifferentWeight() {
    $javascript = drupal_add_js('misc/collapse.js', array('weight' => 2));
    $this->assertEqual($javascript['misc/collapse.js']['weight'], 2, 'Adding a JavaScript file with a different weight caches the given weight.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
