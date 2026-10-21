# JavaScriptTestCase::testAddJsFileWithQueryString()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2035–2039 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2035-L2039)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddJsFileWithQueryString()
```

## Documentation

```text
Tests that the query string remains intact when adding JavaScript files
 that have query string parameters.
```

## Code

```php
  function testAddJsFileWithQueryString() {
    $this->drupalGet('common-test/query-string');
    $query_string = variable_get('css_js_query_string', '0');
    $this->assertRaw(drupal_get_path('module', 'node') . '/node.js?' . $query_string, 'Query string was appended correctly to js.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
