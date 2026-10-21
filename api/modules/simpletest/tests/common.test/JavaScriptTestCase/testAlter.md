# JavaScriptTestCase::testAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1937–1947 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1937-L1947)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlter()
```

## Documentation

```text
Test altering a JavaScript's weight via hook_js_alter().

@see simpletest_js_alter()
```

## Code

```php
  function testAlter() {
    // Add both tableselect.js and simpletest.js, with a larger weight on SimpleTest.
    drupal_add_js('misc/tableselect.js');
    drupal_add_js(drupal_get_path('module', 'simpletest') . '/simpletest.js', array('weight' => 9999));

    // Render the JavaScript, testing if simpletest.js was altered to be before
    // tableselect.js. See simpletest_js_alter() to see where this alteration
    // takes place.
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'simpletest.js') < strpos($javascript, 'misc/tableselect.js'), 'Altering JavaScript weight through the alter hook.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
