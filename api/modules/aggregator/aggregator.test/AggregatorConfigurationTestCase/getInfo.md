# AggregatorConfigurationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 321–327 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L321-L327)
- **Class:** [AggregatorConfigurationTestCase](../AggregatorConfigurationTestCase.md)
- **Module/theme:** aggregator

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
      'name' => 'Aggregator configuration',
      'description' => 'Test aggregator settings page.',
      'group' => 'Aggregator',
    );
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
