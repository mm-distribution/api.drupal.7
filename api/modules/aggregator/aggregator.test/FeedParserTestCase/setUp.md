# FeedParserTestCase::setUp()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 1020–1026 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L1020-L1026)
- **Class:** [FeedParserTestCase](../FeedParserTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    // Do not remove old aggregator items during these tests, since our sample
    // feeds have hardcoded dates in them (which may be expired when this test
    // is run).
    variable_set('aggregator_clear', AGGREGATOR_CLEAR_NEVER);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
