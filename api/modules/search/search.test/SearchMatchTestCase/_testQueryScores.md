# SearchMatchTestCase::_testQueryScores()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 229–243 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L229-L243)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function _testQueryScores($query, $set, $results)
```

## Documentation

```text
Test the scoring abilities of the engine.

Verify if a query produces normalized, monotonous scores.
```

## Code

```php
  function _testQueryScores($query, $set, $results) {
    // Get result scores.
    $scores = array();
    foreach ($set as $item) {
      $scores[] = $item->calculated_score;
    }

    // Check order.
    $sorted = $scores;
    sort($sorted);
    $this->assertEqual($scores, array_reverse($sorted), "Query order '$query'");

    // Check range.
    $this->assertEqual(!count($scores) || (min($scores) > 0.0 && max($scores) <= 1.0001), TRUE, "Query scoring '$query'");
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
