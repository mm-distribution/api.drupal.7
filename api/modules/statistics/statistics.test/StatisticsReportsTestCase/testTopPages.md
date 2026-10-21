# StatisticsReportsTestCase::testTopPages()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 193–197 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L193-L197)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testTopPages()
```

## Documentation

```text
Verifies that 'Top pages' renders properly and displays the added hit.
```

## Code

```php
  function testTopPages() {
    $this->drupalGet('admin/reports/pages');
    $this->assertText('test', 'Hit title found.');
    $this->assertText('node/1', 'Hit URL found.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
