# NodeQueryAlter::testNodeQueryAlterLowLevelEditAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2372–2389 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2372-L2389)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function testNodeQueryAlterLowLevelEditAccess()
```

## Documentation

```text
Tests 'node_access' query alter, for edit access.

Verifies that a non-standard table alias can be used, and that a user with
view-only node access cannot edit the nodes.
```

## Code

```php
  function testNodeQueryAlterLowLevelEditAccess() {
    // User with view-only access should not be able to edit nodes.
    try {
      $query = db_select('node', 'mytab')
        ->fields('mytab');
      $query->addTag('node_access');
      $query->addMetaData('op', 'update');
      $query->addMetaData('account', $this->accessUser);

      $result = $query->execute()->fetchAll();
      $this->assertEqual(count($result), 0, 'User with view-only access cannot edit nodes');
    }
    catch (Exception $e) {
      $this->fail($e->getMessage());
      $this->fail((string) $query);
      $this->fail(t('Altered query is malformed'));
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
