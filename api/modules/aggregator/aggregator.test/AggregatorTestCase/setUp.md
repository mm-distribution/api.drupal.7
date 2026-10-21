# AggregatorTestCase::setUp()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 12–16 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L12-L16)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
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
    parent::setUp('aggregator', 'aggregator_test');
    $web_user = $this->drupalCreateUser(array('administer news feeds', 'access news feeds', 'create article content'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
