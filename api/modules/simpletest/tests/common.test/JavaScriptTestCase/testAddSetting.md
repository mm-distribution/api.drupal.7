# JavaScriptTestCase::testAddSetting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1577–1581 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1577-L1581)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddSetting()
```

## Documentation

```text
Test adding settings.
```

## Code

```php
  function testAddSetting() {
    $javascript = drupal_add_js(array('drupal' => 'rocks', 'dries' => 280342800), 'setting');
    $this->assertEqual(280342800, $javascript['settings']['data'][3]['dries'], 'JavaScript setting is set correctly.');
    $this->assertEqual('rocks', $javascript['settings']['data'][3]['drupal'], 'The other JavaScript setting is set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
