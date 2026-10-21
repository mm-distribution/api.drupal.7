# NodeQueryAlter::testNodeQueryAlterOverride()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2400–2450 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2400-L2450)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function testNodeQueryAlterOverride()
```

## Documentation

```text
Tests 'node_access' query alter override.

Verifies that node_access_view_all_nodes() is called from
node_query_node_access_alter(). We do this by checking that a user who
normally would not have view privileges is able to view the nodes when we
add a record to {node_access} paired with a corresponding privilege in
hook_node_grants().
```

## Code

```php
  function testNodeQueryAlterOverride() {
    $record = array(
      'nid' => 0,
      'gid' => 0,
      'realm' => 'node_access_all',
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
    );
    drupal_write_record('node_access', $record);

    // Test that the noAccessUser still doesn't have the 'view'
    // privilege after adding the node_access record.
    drupal_static_reset('node_access_view_all_nodes');
    try {
      $query = db_select('node', 'mytab')
        ->fields('mytab');
      $query->addTag('node_access');
      $query->addMetaData('op', 'view');
      $query->addMetaData('account', $this->noAccessUser);

      $result = $query->execute()->fetchAll();
      $this->assertEqual(count($result), 0, 'User view privileges are not overridden');
    }
    catch (Exception $e) {
      $this->fail(t('Altered query is malformed'));
    }

    // Have node_test_node_grants return a node_access_all privilege,
    // to grant the noAccessUser 'view' access.  To verify that
    // node_access_view_all_nodes is properly checking the specified
    // $account instead of the global $user, we will log in as
    // noAccessUser2.
    $this->drupalLogin($this->noAccessUser2);
    variable_set('node_test_node_access_all_uid', $this->noAccessUser->uid);
    drupal_static_reset('node_access_view_all_nodes');
    try {
      $query = db_select('node', 'mytab')
        ->fields('mytab');
      $query->addTag('node_access');
      $query->addMetaData('op', 'view');
      $query->addMetaData('account', $this->noAccessUser);

      $result = $query->execute()->fetchAll();
      $this->assertEqual(count($result), 4, 'User view privileges are overridden');
    }
    catch (Exception $e) {
      $this->fail(t('Altered query is malformed'));
    }
    variable_del('node_test_node_access_all_uid');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
