# StatisticsReportsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 172–178 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L172-L178)
- **Class:** [StatisticsReportsTestCase](../StatisticsReportsTestCase.md)
- **Module/theme:** statistics

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Statistics reports tests',
      'description' => 'Tests display of statistics report pages and access logging.',
      'group' => 'Statistics'
    );
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
