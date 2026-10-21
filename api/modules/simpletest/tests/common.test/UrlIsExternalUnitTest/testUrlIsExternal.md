# UrlIsExternalUnitTest::testUrlIsExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 443–447 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L443-L447)
- **Class:** [UrlIsExternalUnitTest](../UrlIsExternalUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUrlIsExternal()
```

## Documentation

```text
Tests if each URL is external or not.
```

## Code

```php
  function testUrlIsExternal() {
    foreach ($this->examples() as $path => $expected) {
      $this->assertIdentical(url_is_external($path), $expected, $path);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
