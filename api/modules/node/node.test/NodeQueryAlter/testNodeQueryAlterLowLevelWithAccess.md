# NodeQueryAlter::testNodeQueryAlterLowLevelWithAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2326–2341 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2326-L2341)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function testNodeQueryAlterLowLevelWithAccess()
```

## Documentation

```text
Tests 'node_access' query alter, for user with access.

Verifies that a non-standard table alias can be used, and that a user with
node access can view the nodes.
```

## Code

```php
  function testNodeQueryAlterLowLevelWithAccess() {
    // User with access should be able to view 4 nodes.
    try {
      $query = db_select('node', 'mytab')
        ->fields('mytab');
      $query->addTag('node_access');
      $query->addMetaData('op', 'view');
      $query->addMetaData('account', $this->accessUser);

      $result = $query->execute()->fetchAll();
      $this->assertEqual(count($result), 4, 'User with access can see correct nodes');
    }
    catch (Exception $e) {
      $this->fail(t('Altered query is malformed'));
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
