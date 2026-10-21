# NodeRevisionPermissionsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2687–2727 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2687-L2727)
- **Class:** [NodeRevisionPermissionsTestCase](../NodeRevisionPermissionsTestCase.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Create a node with several revisions.
    $node = $this->drupalCreateNode();
    $this->node_revisions[] = $node;

    for ($i = 0; $i < 3; $i++) {
      // Create a revision for the same nid and settings with a random log.
      $revision = clone $node;
      $revision->revision = 1;
      $revision->log = $this->randomName(32);
      node_save($revision);
      $this->node_revisions[] = $revision;
    }

    // Create three users, one with each revision permission.
    foreach ($this->map as $op => $permission) {
      // Create the user.
      $account = $this->drupalCreateUser(
        array(
          'access content',
          'edit any page content',
          'delete any page content',
          $permission,
        )
      );
      $account->op = $op;
      $this->accounts[] = $account;
    }

    // Create an admin account (returns TRUE for all revision permissions).
    $admin_account = $this->drupalCreateUser(array('access content', 'administer nodes'));
    $admin_account->is_admin = TRUE;
    $this->accounts['admin'] = $admin_account;

    // Create a normal account (returns FALSE for all revision permissions).
    $normal_account = $this->drupalCreateUser();
    $normal_account->op = FALSE;
    $this->accounts[] = $normal_account;
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
