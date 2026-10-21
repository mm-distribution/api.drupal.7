# JavaScriptTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1535–1546 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1535-L1546)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Enable Locale and SimpleTest in the test environment.
    parent::setUp('locale', 'simpletest', 'common_test');

    // Disable preprocessing
    $this->preprocess_js = variable_get('preprocess_js', 0);
    variable_set('preprocess_js', 0);

    // Reset drupal_add_js() and drupal_add_library() statics before each test.
    drupal_static_reset('drupal_add_js');
    drupal_static_reset('drupal_add_library');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
