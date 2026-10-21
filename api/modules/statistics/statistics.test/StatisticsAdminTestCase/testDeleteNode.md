# StatisticsAdminTestCase::testDeleteNode()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 379–399 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L379-L399)
- **Class:** [StatisticsAdminTestCase](../StatisticsAdminTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testDeleteNode()
```

## Documentation

```text
Tests that when a node is deleted, the node counter is deleted too.
```

## Code

```php
  function testDeleteNode() {
    variable_set('statistics_count_content_views', 1);

    $this->drupalGet('node/' . $this->test_node->nid);

    $result = db_select('node_counter', 'n')
      ->fields('n', array('nid'))
      ->condition('n.nid', $this->test_node->nid)
      ->execute()
      ->fetchAssoc();
    $this->assertEqual($result['nid'], $this->test_node->nid, 'Verifying that the node counter is incremented.');

    node_delete($this->test_node->nid);

    $result = db_select('node_counter', 'n')
      ->fields('n', array('nid'))
      ->condition('n.nid', $this->test_node->nid)
      ->execute()
      ->fetchAssoc();
    $this->assertFalse($result, 'Verifying that the node counter is deleted.');
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
