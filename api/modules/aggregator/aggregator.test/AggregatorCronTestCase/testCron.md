# AggregatorCronTestCase::testCron()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 878–907 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L878-L907)
- **Class:** [AggregatorCronTestCase](../AggregatorCronTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
public function testCron()
```

## Documentation

```text
Adds feeds and updates them via cron process.
```

## Code

```php
  public function testCron() {
    // Create feed and test basic updating on cron.
    $this->createSampleNodes();
    $feed = $this->createFeed();
    $this->cronRun();
    $this->assertEqual(5, db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField(), 'Expected number of items in database.');
    $this->removeFeedItems($feed);
    $this->assertEqual(0, db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField(), 'Expected number of items in database.');
    $this->cronRun();
    $this->assertEqual(5, db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField(), 'Expected number of items in database.');

    // Test feed locking when queued for update.
    $this->removeFeedItems($feed);
    db_update('aggregator_feed')
      ->condition('fid', $feed->fid)
      ->fields(array(
        'queued' => REQUEST_TIME,
      ))
      ->execute();
    $this->cronRun();
    $this->assertEqual(0, db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField(), 'Expected number of items in database.');
    db_update('aggregator_feed')
      ->condition('fid', $feed->fid)
      ->fields(array(
        'queued' => 0,
      ))
      ->execute();
    $this->cronRun();
    $this->assertEqual(5, db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField(), 'Expected number of items in database.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
