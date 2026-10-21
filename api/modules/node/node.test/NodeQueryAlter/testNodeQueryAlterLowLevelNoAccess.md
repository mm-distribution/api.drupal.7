# NodeQueryAlter::testNodeQueryAlterLowLevelNoAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2349–2364 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2349-L2364)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function testNodeQueryAlterLowLevelNoAccess()
```

## Documentation

```text
Tests 'node_access' query alter, for user without access.

Verifies that a non-standard table alias can be used, and that a user
without node access cannot view the nodes.
```

## Code

```php
  function testNodeQueryAlterLowLevelNoAccess() {
    // User without access should be able to view 0 nodes.
    try {
      $query = db_select('node', 'mytab')
        ->fields('mytab');
      $query->addTag('node_access');
      $query->addMetaData('op', 'view');
      $query->addMetaData('account', $this->noAccessUser);

      $result = $query->execute()->fetchAll();
      $this->assertEqual(count($result), 0, 'User with no access cannot see nodes');
    }
    catch (Exception $e) {
      $this->fail(t('Altered query is malformed'));
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
