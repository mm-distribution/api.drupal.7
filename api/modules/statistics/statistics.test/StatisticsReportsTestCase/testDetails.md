# StatisticsReportsTestCase::testDetails()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 210–215 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L210-L215)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testDetails()
```

## Documentation

```text
Verifies that 'Details' page renders properly and displays the added hit.
```

## Code

```php
  function testDetails() {
    $this->drupalGet('admin/reports/access/1');
    $this->assertText('test', 'Hit title found.');
    $this->assertText('node/1', 'Hit URL found.');
    $this->assertText('Anonymous', 'Hit user found.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
