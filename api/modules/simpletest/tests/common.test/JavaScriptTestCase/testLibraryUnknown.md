# JavaScriptTestCase::testLibraryUnknown()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1990–1999 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1990-L1999)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLibraryUnknown()
```

## Documentation

```text
Tests non-existing libraries.
```

## Code

```php
  function testLibraryUnknown() {
    $result = drupal_get_library('unknown', 'unknown');
    $this->assertFalse($result, 'Unknown library returned FALSE.');
    drupal_static_reset('drupal_get_library');

    $result = drupal_add_library('unknown', 'unknown');
    $this->assertFalse($result, 'Unknown library returned FALSE.');
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, 'unknown') === FALSE, 'Unknown library was not added to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
