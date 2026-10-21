# StatisticsTokenReplaceTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 466–472 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L466-L472)
- **Class:** [StatisticsTokenReplaceTestCase](../StatisticsTokenReplaceTestCase.md)
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
      'name' => 'Statistics token replacement',
      'description' => 'Generates text using placeholders for dummy content to check statistics token replacement.',
      'group' => 'Statistics',
    );
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
