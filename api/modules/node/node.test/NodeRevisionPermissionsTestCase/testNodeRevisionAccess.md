# NodeRevisionPermissionsTestCase::testNodeRevisionAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2732–2761 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2732-L2761)
- **Class:** [NodeRevisionPermissionsTestCase](../NodeRevisionPermissionsTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeRevisionAccess()
```

## Documentation

```text
Tests the _node_revision_access() function.
```

## Code

```php
  function testNodeRevisionAccess() {
    $revision = $this->node_revisions[1];

    $parameters = array(
      'op' => array_keys($this->map),
      'account' => $this->accounts,
    );

    $permutations = $this->generatePermutations($parameters);
    foreach ($permutations as $case) {
      if (!empty($case['account']->is_admin) || $case['op'] == $case['account']->op) {
        $this->assertTrue(_node_revision_access($revision, $case['op'], $case['account']), "{$this->map[$case['op']]} granted.");
      }
      else {
        $this->assertFalse(_node_revision_access($revision, $case['op'], $case['account']), "{$this->map[$case['op']]} not granted.");
      }
    }

    // Test that access is FALSE for a node administrator with an invalid $node
    // or $op parameters.
    $admin_account = $this->accounts['admin'];
    $this->assertFalse(_node_revision_access(FALSE, 'view', $admin_account), '_node_revision_access() returns FALSE with an invalid node.');
    $this->assertFalse(_node_revision_access($revision, 'invalid-op', $admin_account), '_node_revision_access() returns FALSE with an invalid op.');

    // Test that the $account parameter defaults to the "logged in" user.
    $original_user = $GLOBALS['user'];
    $GLOBALS['user'] = $admin_account;
    $this->assertTrue(_node_revision_access($revision, 'view'), '_node_revision_access() returns TRUE when used with global user.');
    $GLOBALS['user'] = $original_user;
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
