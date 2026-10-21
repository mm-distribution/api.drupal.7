# UserRolesAssignmentTestCase::testAssignAndRemoveRole()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2829–2844 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2829-L2844)
- **Class:** [UserRolesAssignmentTestCase](../UserRolesAssignmentTestCase.md)
- **Module/theme:** user

## Signature

```php
function testAssignAndRemoveRole()
```

## Documentation

```text
Tests that a user can be assigned a role and that the role can be removed
again.
```

## Code

```php
  function testAssignAndRemoveRole()  {
    $rid = $this->drupalCreateRole(array('administer content types'));
    $account = $this->drupalCreateUser();

    // Assign the role to the user.
    $this->drupalPost('user/' . $account->uid . '/edit', array("roles[$rid]" => $rid), t('Save'));
    $this->assertText(t('The changes have been saved.'));
    $this->assertFieldChecked('edit-roles-' . $rid, 'Role is assigned.');
    $this->userLoadAndCheckRoleAssigned($account, $rid);

    // Remove the role from the user.
    $this->drupalPost('user/' . $account->uid . '/edit', array("roles[$rid]" => FALSE), t('Save'));
    $this->assertText(t('The changes have been saved.'));
    $this->assertNoFieldChecked('edit-roles-' . $rid, 'Role is removed from user.');
    $this->userLoadAndCheckRoleAssigned($account, $rid, FALSE);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
