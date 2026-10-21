# JavaScriptTestCase::testFooterHTML()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1661–1666 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1661-L1666)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFooterHTML()
```

## Documentation

```text
Test drupal_get_js() with a footer scope.
```

## Code

```php
  function testFooterHTML() {
    $inline = 'jQuery(function () { });';
    drupal_add_js($inline, array('type' => 'inline', 'scope' => 'footer'));
    $javascript = drupal_get_js('footer');
    $this->assertTrue(strpos($javascript, $inline) > 0, 'Rendered JavaScript footer returns the inline code.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
