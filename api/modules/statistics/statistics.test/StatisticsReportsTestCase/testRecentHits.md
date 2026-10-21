# StatisticsReportsTestCase::testRecentHits()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 183–188 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L183-L188)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testRecentHits()
```

## Documentation

```text
Verifies that 'Recent hits' renders properly and displays the added hit.
```

## Code

```php
  function testRecentHits() {
    $this->drupalGet('admin/reports/hits');
    $this->assertText('test', 'Hit title found.');
    $this->assertText('node/1', 'Hit URL found.');
    $this->assertText('Anonymous', 'Hit user found.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
