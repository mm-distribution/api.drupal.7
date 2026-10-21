# AggregatorUpdatePathTestCase::testAggregatorUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.aggregator.test`](../_file.md), lines 32–46 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test#L32-L46)
- **Class:** [AggregatorUpdatePathTestCase](../AggregatorUpdatePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testAggregatorUpdate()
```

## Documentation

```text
Tests that the aggregator.module update is successful.
```

## Code

```php
  public function testAggregatorUpdate() {
    // Get a selection of the fields affected by the schema update.
    $query = db_select('aggregator_feed', 'af');
    $query->join('aggregator_item', 'ai', 'af.fid = ai.fid');
    $query
      ->fields('af', array('url', 'link'))
      ->fields('ai', array('link', 'guid'));
    $query->orderBy('ai.iid');

    $pre_update_data = $query->execute()->fetchAll();
    $this->assertTrue($this->performUpgrade(), 'The update was completed successfully.');
    $post_update_data = $query->execute()->fetchAll();

    $this->assertTrue($pre_update_data == $post_update_data, 'Feed data was preserved during the update.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
