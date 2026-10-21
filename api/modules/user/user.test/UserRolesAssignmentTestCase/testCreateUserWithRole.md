# UserRolesAssignmentTestCase::testCreateUserWithRole()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2850–2874 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2850-L2874)
- **Class:** [UserRolesAssignmentTestCase](../UserRolesAssignmentTestCase.md)
- **Module/theme:** user

## Signature

```php
function testCreateUserWithRole()
```

## Documentation

```text
Tests that when creating a user the role can be assigned. And that it can
be removed again.
```

## Code

```php
  function testCreateUserWithRole() {
    $rid = $this->drupalCreateRole(array('administer content types'));
    // Create a new user and add the role at the same time.
    $edit = array(
      'name' => $this->randomName(),
      'mail' => $this->randomName() . '@example.com',
      'pass[pass1]' => $pass = $this->randomString(),
      'pass[pass2]' => $pass,
      "roles[$rid]" => $rid,
    );
    $this->drupalPost('admin/people/create', $edit, t('Create new account'));
    $this->assertText(t('Created a new user account for !name.', array('!name' => $edit['name'])));
    // Get the newly added user.
    $account = user_load_by_name($edit['name']);

    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->assertFieldChecked('edit-roles-' . $rid, 'Role is assigned.');
    $this->userLoadAndCheckRoleAssigned($account, $rid);

    // Remove the role again.
    $this->drupalPost('user/' . $account->uid . '/edit', array("roles[$rid]" => FALSE), t('Save'));
    $this->assertText(t('The changes have been saved.'));
    $this->assertNoFieldChecked('edit-roles-' . $rid, 'Role is removed from user.');
    $this->userLoadAndCheckRoleAssigned($account, $rid, FALSE);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
