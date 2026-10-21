# StatisticsAdminTestCase::testExpiredLogs()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 431–459 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L431-L459)
- **Class:** [StatisticsAdminTestCase](../StatisticsAdminTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testExpiredLogs()
```

## Documentation

```text
Tests that cron clears day counts and expired access logs.
```

## Code

```php
  function testExpiredLogs() {
    variable_set('statistics_enable_access_log', 1);
    variable_set('statistics_count_content_views', 1);
    variable_set('statistics_day_timestamp', 8640000);
    variable_set('statistics_flush_accesslog_timer', 1);

    $this->drupalGet('node/' . $this->test_node->nid);
    $this->drupalGet('node/' . $this->test_node->nid);
    $this->assertText('1 read', 'Node is read once.');

    $this->drupalGet('admin/reports/pages');
    $this->assertText('node/' . $this->test_node->nid, 'Hit URL found.');

    // statistics_cron will subtract the statistics_flush_accesslog_timer
    // variable from REQUEST_TIME in the delete query, so wait two secs here to
    // make sure the access log will be flushed for the node just hit.
    sleep(2);
    $this->cronRun();

    $this->drupalGet('admin/reports/pages');
    $this->assertNoText('node/' . $this->test_node->nid, 'No hit URL found.');

    $result = db_select('node_counter', 'nc')
      ->fields('nc', array('daycount'))
      ->condition('nid', $this->test_node->nid, '=')
      ->execute()
      ->fetchField();
    $this->assertFalse($result, 'Daycounter is zero.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
