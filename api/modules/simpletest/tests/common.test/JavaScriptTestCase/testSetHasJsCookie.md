# JavaScriptTestCase::testSetHasJsCookie()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2044–2051 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2044-L2051)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSetHasJsCookie()
```

## Documentation

```text
Tests that the set_has_js_cookie variable is reflected in Drupal.settings.
```

## Code

```php
  function testSetHasJsCookie() {
    $this->drupalGet('');
    $this->assertRaw('"setHasJsCookie":0', 'setHasJsCookie set to 0 by default.');

    variable_set('set_has_js_cookie', TRUE);
    $this->drupalGet('');
    $this->assertRaw('"setHasJsCookie":1', 'setHasJsCookie set to 1 when set_has_js_cookie is set to TRUE.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
