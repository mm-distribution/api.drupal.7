# JavaScriptTestCase::testAddExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1586–1590 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1586-L1590)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddExternal()
```

## Documentation

```text
Tests adding an external JavaScript File.
```

## Code

```php
  function testAddExternal() {
    $path = 'http://example.com/script.js';
    $javascript = drupal_add_js($path, 'external');
    $this->assertTrue(array_key_exists('http://example.com/script.js', $javascript), 'Added an external JavaScript file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
