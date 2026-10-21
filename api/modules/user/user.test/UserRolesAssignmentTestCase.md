# UserRolesAssignmentTestCase

- **Type:** Class
- **File:** [`modules/user/user.test`](_file.md), lines 2808–2896 · [local source](../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2808-L2896)
- **Module/theme:** user

## Signature

```php
class UserRolesAssignmentTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test role assignment.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](UserRolesAssignmentTestCase/getInfo.md)
- [setUp()](UserRolesAssignmentTestCase/setUp.md)
- [testAssignAndRemoveRole()](UserRolesAssignmentTestCase/testAssignAndRemoveRole.md) — Tests that a user can be assigned a role and that the role can be removed again.
- [testCreateUserWithRole()](UserRolesAssignmentTestCase/testCreateUserWithRole.md) — Tests that when creating a user the role can be assigned. And that it can be removed again.
- [userLoadAndCheckRoleAssigned()](UserRolesAssignmentTestCase/userLoadAndCheckRoleAssigned.md) — Check role on user object.

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
