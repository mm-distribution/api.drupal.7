# UserRolesAssignmentTestCase::userLoadAndCheckRoleAssigned()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2887–2895 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2887-L2895)
- **Class:** [UserRolesAssignmentTestCase](../UserRolesAssignmentTestCase.md)
- **Module/theme:** user

## Signature

```php
private function userLoadAndCheckRoleAssigned($account, $rid, $is_assigned = TRUE)
```

## Documentation

```text
Check role on user object.

@param object $account
  The user account to check.
@param string $rid
  The role ID to search for.
@param bool $is_assigned
  (optional) Whether to assert that $rid exists (TRUE) or not (FALSE).
  Defaults to TRUE.
```

## Code

```php
  private function userLoadAndCheckRoleAssigned($account, $rid, $is_assigned = TRUE) {
    $account = user_load($account->uid, TRUE);
    if ($is_assigned) {
      $this->assertTrue(array_key_exists($rid, $account->roles), 'The role is present in the user object.');
    }
    else {
      $this->assertFalse(array_key_exists($rid, $account->roles), 'The role is not present in the user object.');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
