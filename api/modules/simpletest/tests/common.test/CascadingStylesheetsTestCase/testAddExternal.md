# CascadingStylesheetsTestCase::testAddExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 803–807 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L803-L807)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddExternal()
```

## Documentation

```text
Tests adding an external stylesheet.
```

## Code

```php
  function testAddExternal() {
    $path = 'http://example.com/style.css';
    $css = drupal_add_css($path, 'external');
    $this->assertEqual($css[$path]['type'], 'external', 'Adding an external CSS file caches it properly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
