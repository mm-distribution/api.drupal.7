# AggregatorTestCase::createSampleNodes()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 305–314 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L305-L314)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function createSampleNodes($count = 5)
```

## Documentation

```text
Creates sample article nodes.

@param $count
  (optional) The number of nodes to generate. Defaults to five.
```

## Code

```php
  function createSampleNodes($count = 5) {
    $langcode = LANGUAGE_NONE;
    // Post $count article nodes.
    for ($i = 0; $i < $count; $i++) {
      $edit = array();
      $edit['title'] = $this->randomName();
      $edit["body[$langcode][0][value]"] = $this->randomName();
      $this->drupalPost('node/add/article', $edit, t('Save'));
    }
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
