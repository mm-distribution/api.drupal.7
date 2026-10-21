# CascadingStylesheetsTestCase::testRenderInlineNoPreprocess()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 882–887 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L882-L887)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderInlineNoPreprocess()
```

## Documentation

```text
Tests rendering inline stylesheets with preprocessing off.
```

## Code

```php
  function testRenderInlineNoPreprocess() {
    $css = 'body { padding: 0px; }';
    drupal_add_css($css, array('type' => 'inline', 'preprocess' => FALSE));
    $styles = drupal_get_css();
    $this->assertTrue(strpos($styles, $css) > 0, 'Rendering non-preprocessed inline CSS adds it to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
