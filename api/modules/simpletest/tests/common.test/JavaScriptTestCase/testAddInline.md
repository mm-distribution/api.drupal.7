# JavaScriptTestCase::testAddInline()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1639–1645 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1639-L1645)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddInline()
```

## Documentation

```text
Test adding inline scripts.
```

## Code

```php
  function testAddInline() {
    $inline = 'jQuery(function () { });';
    $javascript = drupal_add_js($inline, array('type' => 'inline', 'scope' => 'footer'));
    $this->assertTrue(array_key_exists('misc/jquery.js', $javascript), 'jQuery is added when inline scripts are added.');
    $data = end($javascript);
    $this->assertEqual($inline, $data['data'], 'Inline JavaScript is correctly added to the footer.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
