# UserPermissionsTestCase::testUserPermissionChanges()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1704–1728 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1704-L1728)
- **Class:** [UserPermissionsTestCase](../UserPermissionsTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPermissionChanges()
```

## Documentation

```text
Change user permissions and check user_access().
```

## Code

```php
  function testUserPermissionChanges() {
    $this->drupalLogin($this->admin_user);
    $rid = $this->rid;
    $account = $this->admin_user;

    // Add a permission.
    $this->assertFalse(user_access('administer nodes', $account), 'User does not have "administer nodes" permission.');
    $edit = array();
    $edit[$rid . '[administer nodes]'] = TRUE;
    $this->drupalPost('admin/people/permissions', $edit, t('Save permissions'));
    $this->assertText(t('The changes have been saved.'), 'Successful save message displayed.');
    drupal_static_reset('user_access');
    drupal_static_reset('user_role_permissions');
    $this->assertTrue(user_access('administer nodes', $account), 'User now has "administer nodes" permission.');

    // Remove a permission.
    $this->assertTrue(user_access('access user profiles', $account), 'User has "access user profiles" permission.');
    $edit = array();
    $edit[$rid . '[access user profiles]'] = FALSE;
    $this->drupalPost('admin/people/permissions', $edit, t('Save permissions'));
    $this->assertText(t('The changes have been saved.'), 'Successful save message displayed.');
    drupal_static_reset('user_access');
    drupal_static_reset('user_role_permissions');
    $this->assertFalse(user_access('access user profiles', $account), 'User no longer has "access user profiles" permission.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
