# StatisticsReportsTestCase::testTopReferrers()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 202–205 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L202-L205)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testTopReferrers()
```

## Documentation

```text
Verifies that 'Top referrers' renders properly and displays the added hit.
```

## Code

```php
  function testTopReferrers() {
    $this->drupalGet('admin/reports/referrers');
    $this->assertText('http://example.com', 'Hit referrer found.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
