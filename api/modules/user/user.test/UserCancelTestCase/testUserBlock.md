# UserCancelTestCase::testUserBlock()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1094–1124 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1094-L1124)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserBlock()
```

## Documentation

```text
Disable account and keep all content.
```

## Code

```php
  function testUserBlock() {
    variable_set('user_cancel_method', 'user_cancel_block');

    // Create a user.
    $web_user = $this->drupalCreateUser(array('cancel account'));
    $this->drupalLogin($web_user);

    // Load real user object.
    $account = user_load($web_user->uid, TRUE);

    // Attempt to cancel account.
    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('Are you sure you want to cancel your account?'), 'Confirmation form to cancel account displayed.');
    $this->assertText(t('Your account will be blocked and you will no longer be able to log in. All of your content will remain attributed to your user name.'), 'Informs that all content will be remain as is.');
    $this->assertNoText(t('Select the method to cancel the account above.'), 'Does not allow user to select account cancellation method.');

    // Confirm account cancellation.
    $timestamp = time();

    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');

    // Confirm account cancellation request.
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $account = user_load($account->uid, TRUE);
    $this->assertTrue($account->status == 0, 'User has been blocked.');

    // Confirm that the confirmation message made it through to the end user.
    $this->assertRaw(t('%name has been disabled.', array('%name' => $account->name)), "Confirmation message displayed to user.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
