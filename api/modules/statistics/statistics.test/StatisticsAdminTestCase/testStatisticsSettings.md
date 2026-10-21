# StatisticsAdminTestCase::testStatisticsSettings()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 347–374 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L347-L374)
- **Class:** [StatisticsAdminTestCase](../StatisticsAdminTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testStatisticsSettings()
```

## Documentation

```text
Verifies that the statistics settings page works.
```

## Code

```php
  function testStatisticsSettings() {
    $this->assertFalse(variable_get('statistics_enable_access_log', 0), 'Access log is disabled by default.');
    $this->assertFalse(variable_get('statistics_count_content_views', 0), 'Count content view log is disabled by default.');

    $this->drupalGet('admin/reports/pages');
    $this->assertRaw(t('No statistics available.'), 'Verifying text shown when no statistics is available.');

    // Enable access log and counter on content view.
    $edit['statistics_enable_access_log'] = 1;
    $edit['statistics_count_content_views'] = 1;
    $this->drupalPost('admin/config/system/statistics', $edit, t('Save configuration'));
    $this->assertTrue(variable_get('statistics_enable_access_log'), 'Access log is enabled.');
    $this->assertTrue(variable_get('statistics_count_content_views'), 'Count content view log is enabled.');

    // Hit the node.
    $this->drupalGet('node/' . $this->test_node->nid);

    $this->drupalGet('admin/reports/pages');
    $this->assertText('node/1', 'Test node found.');

    // Hit the node again (the counter is incremented after the hit, so
    // "1 read" will actually be shown when the node is hit the second time).
    $this->drupalGet('node/' . $this->test_node->nid);
    $this->assertText('1 read', 'Node is read once.');

    $this->drupalGet('node/' . $this->test_node->nid);
    $this->assertText('2 reads', 'Node is read 2 times.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
