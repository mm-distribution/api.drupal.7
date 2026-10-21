# JavaScriptTestCase::testAggregationOrder()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1839–1876 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1839-L1876)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAggregationOrder()
```

## Documentation

```text
Tests JavaScript aggregation when files are added to a different scope.
```

## Code

```php
  function testAggregationOrder() {
    // Enable JavaScript aggregation.
    variable_set('preprocess_js', 1);
    drupal_static_reset('drupal_add_js');

    // Add two JavaScript files to the current request and build the cache.
    drupal_add_js('misc/ajax.js');
    drupal_add_js('misc/autocomplete.js');

    $js_items = drupal_add_js();
    drupal_build_js_cache(array(
      'misc/ajax.js' => $js_items['misc/ajax.js'],
      'misc/autocomplete.js' => $js_items['misc/autocomplete.js']
    ));

    // Store the expected key for the first item in the cache.
    $cache = array_keys(variable_get('drupal_js_cache_files', array()));
    $expected_key = $cache[0];

    // Reset variables and add a file in a different scope first.
    variable_del('drupal_js_cache_files');
    drupal_static_reset('drupal_add_js');
    drupal_add_js('some/custom/javascript_file.js', array('scope' => 'footer'));
    drupal_add_js('misc/ajax.js');
    drupal_add_js('misc/autocomplete.js');

    // Rebuild the cache.
    $js_items = drupal_add_js();
    drupal_build_js_cache(array(
      'misc/ajax.js' => $js_items['misc/ajax.js'],
      'misc/autocomplete.js' => $js_items['misc/autocomplete.js']
    ));

    // Compare the expected key for the first file to the current one.
    $cache = array_keys(variable_get('drupal_js_cache_files', array()));
    $key = $cache[0];
    $this->assertEqual($key, $expected_key, 'JavaScript aggregation is not affected by ordering in different scopes.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
