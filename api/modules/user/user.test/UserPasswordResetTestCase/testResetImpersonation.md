# UserPasswordResetTestCase::testResetImpersonation()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 858–921 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L858-L921)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testResetImpersonation()
```

## Documentation

```text
Make sure that users cannot forge password reset URLs of other users.
```

## Code

```php
  function testResetImpersonation() {
    // Make sure user 1 has a valid password, so it does not interfere with the
    // test user accounts that are created below.
    $account = user_load(1);
    user_save($account, array('pass' => user_password()));

    // Create two identical user accounts except for the user name. They must
    // have the same empty password, so we can't use $this->drupalCreateUser().
    $edit = array();
    $edit['name'] = $this->randomName();
    $edit['mail'] = $edit['name'] . '@example.com';
    $edit['status'] = 1;

    $user1 = user_save(drupal_anonymous_user(), $edit);

    $edit['name'] = $this->randomName();
    $user2 = user_save(drupal_anonymous_user(), $edit);

    // The password reset URL must not be valid for the second user when only
    // the user ID is changed in the URL.
    $reset_url = user_pass_reset_url($user1);
    $attack_reset_url = str_replace("user/reset/$user1->uid", "user/reset/$user2->uid", $reset_url);
    $this->drupalGet($attack_reset_url);
    $this->assertNoText($user2->name, 'The invalid password reset page does not show the user name.');
    $this->assertUrl('user/password', array(), 'The user is redirected to the password reset request page.');
    $this->assertText('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.');

    // When legacy code calls user_pass_rehash() without providing the $uid
    // parameter, neither password reset URL should be valid since it is
    // impossible for the system to determine which user account the token was
    // intended for.
    $timestamp = REQUEST_TIME;
    // Pass an explicit NULL for the $uid parameter of user_pass_rehash()
    // rather than not passing it at all, to avoid triggering PHP warnings in
    // the test.
    $reset_url_token = user_pass_rehash($user1->pass, $timestamp, $user1->login, NULL);
    $reset_url = url("user/reset/$user1->uid/$timestamp/$reset_url_token", array('absolute' => TRUE));
    $this->drupalGet($reset_url);
    $this->assertNoText($user1->name, 'The invalid password reset page does not show the user name.');
    $this->assertUrl('user/password', array(), 'The user is redirected to the password reset request page.');
    $this->assertText('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.');
    $attack_reset_url = str_replace("user/reset/$user1->uid", "user/reset/$user2->uid", $reset_url);
    $this->drupalGet($attack_reset_url);
    $this->assertNoText($user2->name, 'The invalid password reset page does not show the user name.');
    $this->assertUrl('user/password', array(), 'The user is redirected to the password reset request page.');
    $this->assertText('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.');

    // To verify that user_pass_rehash() never returns a valid result in the
    // above situation (even if legacy code also called it to attempt to
    // validate the token, rather than just to generate the URL), check that a
    // second call with the same parameters produces a different result.
    $new_reset_url_token = user_pass_rehash($user1->pass, $timestamp, $user1->login, NULL);
    $this->assertNotEqual($reset_url_token, $new_reset_url_token);

    // However, when the duplicate account is removed, the password reset URL
    // should be valid.
    user_delete($user2->uid);
    $reset_url_token = user_pass_rehash($user1->pass, $timestamp, $user1->login, NULL);
    $reset_url = url("user/reset/$user1->uid/$timestamp/$reset_url_token", array('absolute' => TRUE));
    $this->drupalGet($reset_url);
    $this->assertText($user1->name, 'The valid password reset page shows the user name.');
    $this->assertUrl($this->getConfirmURL($reset_url), array(), 'The user is redirected to the reset password confirm form.');
    $this->assertNoText('You have tried to use a one-time login link that has either been used or is no longer valid. Please request a new one using the form below.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
