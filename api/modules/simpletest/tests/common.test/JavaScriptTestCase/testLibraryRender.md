# JavaScriptTestCase::testLibraryRender()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1952–1959 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1952-L1959)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLibraryRender()
```

## Documentation

```text
Adds a library to the page and tests for both its JavaScript and its CSS.
```

## Code

```php
  function testLibraryRender() {
    $result = drupal_add_library('system', 'farbtastic');
    $this->assertTrue($result !== FALSE, 'Library was added without errors.');
    $scripts = drupal_get_js();
    $styles = drupal_get_css();
    $this->assertTrue(strpos($scripts, 'misc/farbtastic/farbtastic.js'), 'JavaScript of library was added to the page.');
    $this->assertTrue(strpos($styles, 'misc/farbtastic/farbtastic.css'), 'Stylesheet of library was added to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
