# CascadingStylesheetsTestCase::testAddCssFileWithQueryString()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 998–1003 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L998-L1003)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAddCssFileWithQueryString()
```

## Documentation

```text
Tests that the query string remains intact when adding CSS files that have
query string parameters.
```

## Code

```php
  function testAddCssFileWithQueryString() {
    $this->drupalGet('common-test/query-string');
    $query_string = variable_get('css_js_query_string', '0');
    $this->assertRaw(drupal_get_path('module', 'node') . '/node.css?' . $query_string, 'Query string was appended correctly to css.');
    $this->assertRaw(drupal_get_path('module', 'node') . '/node-fake.css?arg1=value1&amp;arg2=value2', 'Query string not escaped on a URI.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
