# CascadingStylesheetsTestCase::testRenderExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 834–841 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L834-L841)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderExternal()
```

## Documentation

```text
Tests rendering an external stylesheet.
```

## Code

```php
  function testRenderExternal() {
    $css = 'http://example.com/style.css';
    drupal_add_css($css, 'external');
    $styles = drupal_get_css();
    // Stylesheet URL may be the href of a LINK tag or in an @import statement
    // of a STYLE tag.
    $this->assertTrue(strpos($styles, 'href="' . $css) > 0 || strpos($styles, '@import url("' . $css . '")') > 0, 'Rendering an external CSS file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
