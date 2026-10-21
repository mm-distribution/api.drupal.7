# UserPasswordResetTestCase::testUserPasswordResetLoggedIn()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 738–797 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L738-L797)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPasswordResetLoggedIn($use_direct_login_link = FALSE)
```

## Documentation

```text
Test user password reset while logged in.
```

## Code

```php
  function testUserPasswordResetLoggedIn($use_direct_login_link = FALSE) {
    $another_account = $this->drupalCreateUser();
    $account = $this->drupalCreateUser();
    $this->drupalLogin($account);
    // Make sure the test account has a valid password.
    user_save($account, array('pass' => user_password()));

    // Try to use the login link while logged in as a different user.
    // Generate one time login link.
    $reset_url = $this->generateResetURL($another_account, $use_direct_login_link);
    $this->drupalGet($reset_url);
    $this->assertRaw(t(
      'Another user (%other_user) is already logged into the site on this computer, but you tried to use a one-time link for user %resetting_user. Please <a href="!logout">logout</a> and try using the link again.',
      array('%other_user' => $account->name, '%resetting_user' => $another_account->name, '!logout' => url('user/logout'))
    ));

    // Verify that the invalid password reset page does not show the user name.
    $attack_reset_url = "user/reset/" . $another_account->uid . "/1/1";
    $this->drupalGet($attack_reset_url);
    $this->assertNoText($another_account->name);
    $this->assertText('The one-time login link you clicked is invalid.');

    // Test the link for a deleted user while logged in.
    user_delete($another_account->uid);
    $this->drupalGet($reset_url);
    $this->assertText('The one-time login link you clicked is invalid.');

    // Generate a one time login link for the logged-in user.
    $fapi_action = $use_direct_login_link ? 'build' : 'submit';
    variable_del("user_test_pass_reset_form_{$fapi_action}_{$account->uid}");
    $reset_url = $this->generateResetURL($account, $use_direct_login_link);
    $this->drupalGet($reset_url);
    if ($use_direct_login_link) {
      // The form is never fully built; user is logged out (session destroyed)
      // and redirected to the same URL, then logged in again and redirected
      // during form build.
      $form_built = variable_get("user_test_pass_reset_form_build_{$account->uid}", FALSE);
      $this->assertTrue(!$form_built, 'The password reset form was never fully built.');
    }
    else {
      $this->assertUrl($this->getConfirmURL($reset_url), array(), 'The user is redirected to the reset password confirm form.');
      $this->assertText('Reset password');
      $this->drupalPost(NULL, NULL, t('Log in'));
      // The form was fully processed before redirecting.
      $form_submit_handled = variable_get("user_test_pass_reset_form_submit_{$account->uid}", FALSE);
      $this->assertTrue($form_submit_handled, 'A custom submit handler executed.');
    }
    $this->assertText('You have just used your one-time login link. It is no longer necessary to use this link to log in. Please change your password.');

    // The user can change the forgotten password on the page they are
    // redirected to.
    $pass = user_password();
    $edit = array(
      'pass[pass1]' => $pass,
      'pass[pass2]' => $pass,
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    $this->assertText('The changes have been saved.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
