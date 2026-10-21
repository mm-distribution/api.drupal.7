# JavaScriptTestCase::testDifferentGroup()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1823–1826 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1823-L1826)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDifferentGroup()
```

## Documentation

```text
Test adding a JavaScript file with a different group.
```

## Code

```php
  function testDifferentGroup() {
    $javascript = drupal_add_js('misc/collapse.js', array('group' => JS_THEME));
    $this->assertEqual($javascript['misc/collapse.js']['group'], JS_THEME, 'Adding a JavaScript file with a different group caches the given group.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
