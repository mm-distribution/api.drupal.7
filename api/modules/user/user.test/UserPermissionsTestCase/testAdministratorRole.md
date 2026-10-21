# UserPermissionsTestCase::testAdministratorRole()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1733–1748 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1733-L1748)
- **Class:** [UserPermissionsTestCase](../UserPermissionsTestCase.md)
- **Module/theme:** user

## Signature

```php
function testAdministratorRole()
```

## Documentation

```text
Test assigning of permissions for the administrator role.
```

## Code

```php
  function testAdministratorRole() {
    $this->drupalLogin($this->admin_user);
    $this->drupalGet('admin/config/people/accounts');

    // Set the user's role to be the administrator role.
    $edit = array();
    $edit['user_admin_role'] = $this->rid;
    $this->drupalPost('admin/config/people/accounts', $edit, t('Save configuration'));

    // Enable aggregator module and ensure the 'administer news feeds'
    // permission is assigned by default.
    $edit = array();
    $edit['modules[Core][aggregator][enable]'] = TRUE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertTrue(user_access('administer news feeds', $this->admin_user), 'The permission was automatically assigned to the administrator role');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
