# StatisticsReportsTestCase::testAccessLogging()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 220–225 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L220-L225)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testAccessLogging()
```

## Documentation

```text
Verifies that access logging is working and is reported correctly.
```

## Code

```php
  function testAccessLogging() {
    $this->drupalGet('admin/reports/referrers');
    $this->drupalGet('admin/reports/hits');
    $this->assertText('Top referrers in the past 3 days', 'Hit title found.');
    $this->assertText('admin/reports/referrers', 'Hit URL found.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
