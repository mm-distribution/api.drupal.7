# JavaScriptTestCase::testRenderDifferentWeight()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1923–1930 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1923-L1930)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderDifferentWeight()
```

## Documentation

```text
Test rendering the JavaScript with a file's weight above jQuery's.
```

## Code

```php
  function testRenderDifferentWeight() {
    // JavaScript files are sorted first by group, then by the 'every_page'
    // flag, then by weight (see drupal_sort_css_js()), so to test the effect of
    // weight, we need the other two options to be the same.
    drupal_add_js('misc/collapse.js', array('group' => JS_LIBRARY, 'every_page' => TRUE, 'weight' => -21));
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') < strpos($javascript, 'misc/jquery.js'), 'Rendering a JavaScript file above jQuery.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
