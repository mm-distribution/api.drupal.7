# AggregatorTestCase::getAtomSample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 285–289 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L285-L289)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getAtomSample()
```

## Documentation

_No docblock in source._

## Code

```php
  function getAtomSample() {
    // The content of this sample ATOM feed is based directly off of the
    // example provided in RFC 4287.
    return $GLOBALS['base_url'] . '/' . drupal_get_path('module', 'aggregator') . '/tests/aggregator_test_atom.xml';
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
