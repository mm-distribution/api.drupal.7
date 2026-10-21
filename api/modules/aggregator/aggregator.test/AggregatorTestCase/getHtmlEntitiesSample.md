# AggregatorTestCase::getHtmlEntitiesSample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 291–293 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L291-L293)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getHtmlEntitiesSample()
```

## Documentation

_No docblock in source._

## Code

```php
  function getHtmlEntitiesSample() {
    return $GLOBALS['base_url'] . '/' . drupal_get_path('module', 'aggregator') . '/tests/aggregator_test_title_entities.xml';
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
