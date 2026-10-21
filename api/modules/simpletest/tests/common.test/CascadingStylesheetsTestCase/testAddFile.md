# CascadingStylesheetsTestCase::testAddFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 794–798 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L794-L798)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddFile()
```

## Documentation

```text
Tests adding a file stylesheet.
```

## Code

```php
  function testAddFile() {
    $path = drupal_get_path('module', 'simpletest') . '/simpletest.css';
    $css = drupal_add_css($path);
    $this->assertEqual($css[$path]['data'], $path, 'Adding a CSS file caches it properly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
