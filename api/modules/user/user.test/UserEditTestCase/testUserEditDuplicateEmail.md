# UserEditTestCase::testUserEditDuplicateEmail()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2348–2378 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2348-L2378)
- **Class:** [UserEditTestCase](../UserEditTestCase.md)
- **Module/theme:** user

## Signature

```php
public function testUserEditDuplicateEmail()
```

## Documentation

```text
Tests that the user can edit the account when another user with the same
e-mail address exists.
```

## Code

```php
  public function testUserEditDuplicateEmail() {
    // Create two regular users.
    $user1 = $this->drupalCreateUser(array('change own username'));
    $user2 = $this->drupalCreateUser(array('change own username'));

    // Change the e-mail address of the user2 to have the same e-mail address
    // as the user1.
    db_update('users')
      ->fields(array('mail' => $user1->mail))
      ->condition('uid', $user2->uid)
      ->execute();

    $this->drupalLogin($user2);
    $edit['name'] = $user2->name;
    $this->drupalPost("user/" . $user2->uid . "/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $this->drupalLogout();

    // Change the e-mail address of the user2 to have the same e-mail address
    // as the user1, except that the first letter will be uppercase.
    db_update('users')
      ->fields(array('mail' => ucfirst($user1->mail)))
      ->condition('uid', $user2->uid)
      ->execute();

    $this->drupalLogin($user2);
    $edit['name'] = $user2->name;
    $this->drupalPost("user/" . $user2->uid . "/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
