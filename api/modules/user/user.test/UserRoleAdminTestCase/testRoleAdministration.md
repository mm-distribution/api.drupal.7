# UserRoleAdminTestCase::testRoleAdministration()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2577–2620 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2577-L2620)
- **Class:** [UserRoleAdminTestCase](../UserRoleAdminTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRoleAdministration()
```

## Documentation

```text
Test adding, renaming and deleting roles.
```

## Code

```php
  function testRoleAdministration() {
    $this->drupalLogin($this->admin_user);

    // Test adding a role. (In doing so, we use a role name that happens to
    // correspond to an integer, to test that the role administration pages
    // correctly distinguish between role names and IDs.)
    $role_name = '123';
    $edit = array('name' => $role_name);
    $this->drupalPost('admin/people/permissions/roles', $edit, t('Add role'));
    $this->assertText(t('The role has been added.'), 'The role has been added.');
    $role = user_role_load_by_name($role_name);
    $this->assertTrue(is_object($role), 'The role was successfully retrieved from the database.');

    // Try adding a duplicate role.
    $this->drupalPost(NULL, $edit, t('Add role'));
    $this->assertRaw(t('The role name %name already exists. Choose another role name.', array('%name' => $role_name)), 'Duplicate role warning displayed.');

    // Test renaming a role.
    $old_name = $role_name;
    $role_name = '456';
    $edit = array('name' => $role_name);
    $this->drupalPost("admin/people/permissions/roles/edit/{$role->rid}", $edit, t('Save role'));
    $this->assertText(t('The role has been renamed.'), 'The role has been renamed.');
    $this->assertFalse(user_role_load_by_name($old_name), 'The role can no longer be retrieved from the database using its old name.');
    $this->assertTrue(is_object(user_role_load_by_name($role_name)), 'The role can be retrieved from the database using its new name.');

    // Test deleting the default administrator role.
    $role_name = 'administrator';
    $role = user_role_load_by_name($role_name);
    $this->drupalPost("admin/people/permissions/roles/edit/{$role->rid}", NULL, t('Delete role'));
    $this->drupalPost(NULL, NULL, t('Delete'));
    $this->assertText(t('The role has been deleted.'), 'The role has been deleted');
    $this->assertNoLinkByHref("admin/people/permissions/roles/edit/{$role->rid}", 'Role edit link removed.');
    $this->assertFalse(user_role_load_by_name($role_name), 'A deleted role can no longer be loaded.');
    // Make sure this role is no longer configured as the administrator role.
    $this->assertNull(variable_get('user_admin_role'), 'The administrator role is no longer configured as the administrator role.');

    // Make sure that the system-defined roles cannot be edited via the user
    // interface.
    $this->drupalGet('admin/people/permissions/roles/edit/' . DRUPAL_ANONYMOUS_RID);
    $this->assertResponse(403, 'Access denied when trying to edit the built-in anonymous role.');
    $this->drupalGet('admin/people/permissions/roles/edit/' . DRUPAL_AUTHENTICATED_RID);
    $this->assertResponse(403, 'Access denied when trying to edit the built-in authenticated role.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
