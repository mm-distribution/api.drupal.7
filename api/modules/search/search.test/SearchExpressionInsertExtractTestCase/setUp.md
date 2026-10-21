# SearchExpressionInsertExtractTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 996–999 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L996-L999)
- **Class:** [SearchExpressionInsertExtractTestCase](../SearchExpressionInsertExtractTestCase.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    drupal_load('module', 'search');
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
