# UserPermissionsTestCase::testUserRoleChangePermissions()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1753–1773 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1753-L1773)
- **Class:** [UserPermissionsTestCase](../UserPermissionsTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserRoleChangePermissions()
```

## Documentation

```text
Verify proper permission changes by user_role_change_permissions().
```

## Code

```php
  function testUserRoleChangePermissions() {
    $rid = $this->rid;
    $account = $this->admin_user;

    // Verify current permissions.
    $this->assertFalse(user_access('administer nodes', $account), 'User does not have "administer nodes" permission.');
    $this->assertTrue(user_access('access user profiles', $account), 'User has "access user profiles" permission.');
    $this->assertTrue(user_access('administer site configuration', $account), 'User has "administer site configuration" permission.');

    // Change permissions.
    $permissions = array(
      'administer nodes' => 1,
      'access user profiles' => 0,
    );
    user_role_change_permissions($rid, $permissions);

    // Verify proper permission changes.
    $this->assertTrue(user_access('administer nodes', $account), 'User now has "administer nodes" permission.');
    $this->assertFalse(user_access('access user profiles', $account), 'User no longer has "access user profiles" permission.');
    $this->assertTrue(user_access('administer site configuration', $account), 'User still has "administer site configuration" permission.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
