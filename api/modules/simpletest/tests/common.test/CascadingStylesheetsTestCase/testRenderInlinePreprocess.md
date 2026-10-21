# CascadingStylesheetsTestCase::testRenderInlinePreprocess()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 846–852 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L846-L852)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderInlinePreprocess()
```

## Documentation

```text
Tests rendering inline stylesheets with preprocessing on.
```

## Code

```php
  function testRenderInlinePreprocess() {
    $css = 'body { padding: 0px; }';
    $css_preprocessed = '<style type="text/css" media="all">' . "\n<!--/*--><![CDATA[/*><!--*/\n" . drupal_load_stylesheet_content($css, TRUE) . "\n/*]]>*/-->\n" . '</style>';
    drupal_add_css($css, array('type' => 'inline'));
    $styles = drupal_get_css();
    $this->assertEqual(trim($styles), $css_preprocessed, 'Rendering preprocessed inline CSS adds it to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
