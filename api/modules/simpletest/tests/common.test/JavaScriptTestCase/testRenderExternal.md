# JavaScriptTestCase::testRenderExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1650–1656 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1650-L1656)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderExternal()
```

## Documentation

```text
Test rendering an external JavaScript file.
```

## Code

```php
  function testRenderExternal() {
    $external = 'http://example.com/example.js';
    drupal_add_js($external, 'external');
    $javascript = drupal_get_js();
    // Local files have a base_path() prefix, external files should not.
    $this->assertTrue(strpos($javascript, 'src="' . $external) > 0, 'Rendering an external JavaScript file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
