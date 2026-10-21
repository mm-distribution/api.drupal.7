# NodeBodyUpgradePathTestCase::testNodeBodyUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.node.test`](../_file.md), lines 28–53 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test#L28-L53)
- **Class:** [NodeBodyUpgradePathTestCase](../NodeBodyUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNodeBodyUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  public function testNodeBodyUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    $instance = field_info_instance('node', 'body', 'story');
    $this->assertIdentical($instance['required'], 0, 'The required setting was preserved during the upgrade path.');
    $this->assertTrue($instance['description'], 'The description was preserved during the upgrade path');

    $this->drupalGet("content/1263769200");
    $this->assertText('node body (broken) - 37');

    // Find a published node revision and make sure it still has a body.
    $revision = db_query_range("SELECT r.nid, r.vid FROM {node_revision} r JOIN {node} n ON n.nid = r.nid WHERE n.status = 1 AND n.type <> 'poll' AND n.vid <> r.vid", 0, 1)->fetch();
    $revision = node_load($revision->nid, $revision->vid);
    $this->assertTrue(!empty($revision->body), 'Non-current node revisions still have a node body.');
    // Find an unpublished node revision and make sure it still has a body.
    $revision = db_query_range("SELECT r.nid, r.vid FROM {node_revision} r JOIN {node} n ON n.nid = r.nid WHERE n.status = 0 AND n.type <> 'poll' AND n.vid <> r.vid", 0, 1)->fetch();
    $revision = node_load($revision->nid, $revision->vid);
    $this->assertTrue(!empty($revision->body), 'Unpublished non-current node revisions still have a node body.');

    // Check that fields created during the upgrade can be edited and resaved
    // in the UI.
    $this->drupalPost('admin/structure/types/manage/story/fields/body', array(), t('Save settings'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.node.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
