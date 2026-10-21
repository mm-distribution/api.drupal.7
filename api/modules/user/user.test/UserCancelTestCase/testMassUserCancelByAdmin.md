# UserCancelTestCase::testMassUserCancelByAdmin()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1311–1359 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1311-L1359)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testMassUserCancelByAdmin()
```

## Documentation

```text
Create an administrative user and mass-delete other users.
```

## Code

```php
  function testMassUserCancelByAdmin() {
    variable_set('user_cancel_method', 'user_cancel_reassign');
    // Enable account cancellation notification.
    variable_set('user_mail_status_canceled_notify', TRUE);

    // Create administrative user.
    $admin_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($admin_user);

    // Create some users.
    $users = array();
    for ($i = 0; $i < 3; $i++) {
      $account = $this->drupalCreateUser(array());
      $users[$account->uid] = $account;
    }

    // Cancel user accounts, including own one.
    $edit = array();
    $edit['operation'] = 'cancel';
    foreach ($users as $uid => $account) {
      $edit['accounts[' . $uid . ']'] = TRUE;
    }
    $edit['accounts[' . $admin_user->uid . ']'] = TRUE;
    // Also try to cancel uid 1.
    $edit['accounts[1]'] = TRUE;
    $this->drupalPost('admin/people', $edit, t('Update'));
    $this->assertText(t('Are you sure you want to cancel these user accounts?'), 'Confirmation form to cancel accounts displayed.');
    $this->assertText(t('When cancelling these accounts'), 'Allows to select account cancellation method.');
    $this->assertText(t('Require e-mail confirmation to cancel account.'), 'Allows to send confirmation mail.');
    $this->assertText(t('Notify user when account is canceled.'), 'Allows to send notification mail.');

    // Confirm deletion.
    $this->drupalPost(NULL, NULL, t('Cancel accounts'));
    $status = TRUE;
    foreach ($users as $account) {
      $status = $status && (strpos($this->content, t('%name has been deleted.', array('%name' => $account->name))) !== FALSE);
      $status = $status && !user_load($account->uid, TRUE);
    }
    $this->assertTrue($status, 'Users deleted and not found in the database.');

    // Ensure that admin account was not cancelled.
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');
    $admin_user = user_load($admin_user->uid);
    $this->assertTrue($admin_user->status == 1, 'Administrative user is found in the database and enabled.');

    // Verify that uid 1's account was not cancelled.
    $user1 = user_load(1, TRUE);
    $this->assertEqual($user1->status, 1, 'User #1 still exists and is not blocked.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
