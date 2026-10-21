# JavaScriptTestCase::testRenderOrder()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1881–1918 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1881-L1918)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderOrder()
```

## Documentation

```text
Test JavaScript ordering.
```

## Code

```php
  function testRenderOrder() {
    // Add a bunch of JavaScript in strange ordering.
    drupal_add_js('(function($){alert("Weight 5 #1");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => 5));
    drupal_add_js('(function($){alert("Weight 0 #1");})(jQuery);', array('type' => 'inline', 'scope' => 'footer'));
    drupal_add_js('(function($){alert("Weight 0 #2");})(jQuery);', array('type' => 'inline', 'scope' => 'footer'));
    drupal_add_js('(function($){alert("Weight -8 #1");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => -8));
    drupal_add_js('(function($){alert("Weight -8 #2");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => -8));
    drupal_add_js('(function($){alert("Weight -8 #3");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => -8));
    drupal_add_js('http://example.com/example.js?Weight -5 #1', array('type' => 'external', 'scope' => 'footer', 'weight' => -5));
    drupal_add_js('(function($){alert("Weight -8 #4");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => -8));
    drupal_add_js('(function($){alert("Weight 5 #2");})(jQuery);', array('type' => 'inline', 'scope' => 'footer', 'weight' => 5));
    drupal_add_js('(function($){alert("Weight 0 #3");})(jQuery);', array('type' => 'inline', 'scope' => 'footer'));

    // Construct the expected result from the regex.
    $expected = array(
      "-8 #1",
      "-8 #2",
      "-8 #3",
      "-8 #4",
      "-5 #1", // The external script.
      "0 #1",
      "0 #2",
      "0 #3",
      "5 #1",
      "5 #2",
    );

    // Retrieve the rendered JavaScript and test against the regex.
    $js = drupal_get_js('footer');
    $matches = array();
    if (preg_match_all('/Weight\s([-0-9]+\s[#0-9]+)/', $js, $matches)) {
      $result = $matches[1];
    }
    else {
      $result = array();
    }
    $this->assertIdentical($result, $expected, 'JavaScript is added in the expected weight order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
