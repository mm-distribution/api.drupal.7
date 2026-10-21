# AggregatorUpdatePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.aggregator.test`](../_file.md), lines 8–14 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test#L8-L14)
- **Class:** [AggregatorUpdatePathTestCase](../AggregatorUpdatePathTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'Aggregator update path',
      'description' => 'Aggregator update path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
