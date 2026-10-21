# AggregatorTestCase::getCategories()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 175–182 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L175-L182)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getCategories()
```

## Documentation

```text
Pulls categories from {aggregator_category} table.

@return
  An associative array keyed by category ID and values are set to the
  category names.
```

## Code

```php
  function getCategories() {
    $categories = array();
    $result = db_query('SELECT * FROM {aggregator_category}');
    foreach ($result as $category) {
      $categories[$category->cid] = $category;
    }
    return $categories;
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
