# common_test_js_and_css_querystring()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 275–281 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L275-L281)
- **Module/theme:** batch_test

## Signature

```php
function common_test_js_and_css_querystring()
```

## Documentation

```text
Adds a JavaScript file and a CSS file with a query string appended.
```

## Code

```php
function common_test_js_and_css_querystring() {
   drupal_add_js(drupal_get_path('module', 'node') . '/node.js');
   drupal_add_css(drupal_get_path('module', 'node') . '/node.css');
   // A relative URI may have a query string.
   drupal_add_css('/' . drupal_get_path('module', 'node') . '/node-fake.css?arg1=value1&arg2=value2');
   return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
