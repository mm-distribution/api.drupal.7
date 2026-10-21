# SearchMatchTestCase::_testQueryMatching()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 211–222 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L211-L222)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function _testQueryMatching($query, $set, $results)
```

## Documentation

```text
Test the matching abilities of the engine.

Verify if a query produces the correct results.
```

## Code

```php
  function _testQueryMatching($query, $set, $results) {
    // Get result IDs.
    $found = array();
    foreach ($set as $item) {
      $found[] = $item->sid;
    }

    // Compare $results and $found.
    sort($found);
    sort($results);
    $this->assertEqual($found, $results, "Query matching '$query'");
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
