# StatisticsBlockVisitorsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 262–268 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L262-L268)
- **Class:** [StatisticsBlockVisitorsTestCase](../StatisticsBlockVisitorsTestCase.md)
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
      'name' => 'Top visitor blocking',
      'description' => 'Tests blocking of IP addresses via the top visitors report.',
      'group' => 'Statistics'
    );
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
