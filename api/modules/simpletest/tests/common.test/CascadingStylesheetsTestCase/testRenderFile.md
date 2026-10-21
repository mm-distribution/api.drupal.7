# CascadingStylesheetsTestCase::testRenderFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 820–829 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L820-L829)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderFile()
```

## Documentation

```text
Tests rendering the stylesheets.
```

## Code

```php
  function testRenderFile() {
    $css = drupal_get_path('module', 'simpletest') . '/simpletest.css';
    drupal_add_css($css);
    $styles = drupal_get_css();
    $this->assertTrue(strpos($styles, $css) > 0, 'Rendered CSS includes the added stylesheet.');
    // Verify that newlines are properly added inside style tags.
    $query_string = variable_get('css_js_query_string', '0');
    $css_processed = "<style type=\"text/css\" media=\"all\">\n@import url(\"" . check_plain(file_create_url($css)) . "?" . $query_string ."\");\n</style>";
    $this->assertEqual(trim($styles), $css_processed, 'Rendered CSS includes newlines inside style tags for JavaScript use.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
