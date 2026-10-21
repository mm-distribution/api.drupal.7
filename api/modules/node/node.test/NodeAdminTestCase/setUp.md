# NodeAdminTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1808–1820 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1808-L1820)
- **Class:** [NodeAdminTestCase](../NodeAdminTestCase.md)
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

    // Remove the "view own unpublished content" permission which is set
    // by default for authenticated users so we can test this permission
    // correctly.
    user_role_revoke_permissions(DRUPAL_AUTHENTICATED_RID, array('view own unpublished content'));

    $this->admin_user = $this->drupalCreateUser(array('access administration pages', 'access content overview', 'administer nodes', 'bypass node access'));
    $this->base_user_1 = $this->drupalCreateUser(array('access content overview'));
    $this->base_user_2 = $this->drupalCreateUser(array('access content overview', 'view own unpublished content'));
    $this->base_user_3 = $this->drupalCreateUser(array('access content overview', 'bypass node access'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
