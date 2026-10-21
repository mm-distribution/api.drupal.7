# UserPasswordResetTestCase::testUserPasswordReset()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 571–653 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L571-L653)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPasswordReset($use_direct_login_link = FALSE)
```

## Documentation

```text
Tests password reset functionality.
```

## Code

```php
  function testUserPasswordReset($use_direct_login_link = FALSE) {
    // Create a user.
    $account = $this->drupalCreateUser();
    $this->drupalLogin($account);
    $this->drupalLogout();
    // Attempt to reset password.
    $edit = array('name' => $account->name);
    $this->drupalPost('user/password', $edit, t('E-mail new password'));
    // Ensure the correct message is shown for a valid user name.
    $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
    $this->assertRaw(format_string($password_reset_text, array('%identifier' => $account->name)), 'Password reset instructions mailed message displayed for a valid user.');

    // Ensure that flood control was not triggered.
    $this->assertNoText(t('is temporarily blocked. Try again later'), 'Flood control was not triggered by single password reset.');

    // Ensure the correct message is shown for a non-existent user name.
    $name = $this->randomName();
    $edit = array('name' => $name);
    $this->drupalPost('user/password', $edit, t('E-mail new password'));
    $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
    $this->assertRaw(format_string($password_reset_text, array('%identifier' => $name)), 'Password reset instructions mailed message displayed for a non-existent user.');

    // Create an image field to enable an Ajax request on the user profile page.
    $field = array(
      'field_name' => 'field_avatar',
      'type' => 'image',
      'settings' => array(),
      'cardinality' => 1,
    );
    field_create_field($field);

    $instance = array(
      'field_name' => $field['field_name'],
      'entity_type' => 'user',
      'label' => 'Avatar',
      'bundle' => 'user',
      'required' => FALSE,
      'settings' => array(),
      'widget' => array(
        'type' => 'image_image',
        'settings' => array(),
      ),
    );
    field_create_instance($instance);

    variable_del("user_test_pass_reset_form_submit_{$account->uid}");
    $resetURL = $this->getResetURL($use_direct_login_link);
    $this->drupalGet($resetURL);

    // Check successful login.
    if (!$use_direct_login_link) {
      $this->assertUrl($this->getConfirmURL($resetURL), array(), 'The user is redirected to the reset password confirm form.');
      $this->drupalPost(NULL, NULL, t('Log in'));
      // The form was fully processed before redirecting.
      $form_submit_handled = variable_get("user_test_pass_reset_form_submit_{$account->uid}", FALSE);
      $this->assertTrue($form_submit_handled, 'A custom submit handler executed.');
    }
    $this->assertText('You have just used your one-time login link. It is no longer necessary to use this link to log in. Please change your password.');

    // Make sure the Ajax request from uploading a file does not invalidate the
    // reset token.
    $image = current($this->drupalGetTestFiles('image'));
    $edit = array(
      'files[field_avatar_und_0]' => drupal_realpath($image->uri),
    );
    $this->drupalPostAJAX(NULL, $edit, 'field_avatar_und_0_upload_button');

    // Change the forgotten password.
    $password = user_password();
    $edit = array('pass[pass1]' => $password, 'pass[pass2]' => $password);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertText(t('The changes have been saved.'), 'Forgotten password changed.');

    // Ensure blocked and deleted accounts can't access the direct login link.
    $this->drupalLogout();
    $reset_url = $this->generateResetURL($account, $use_direct_login_link);
    user_save($account, array('status' => 0));
    $this->drupalGet($reset_url);
    $this->assertResponse(403);
    user_delete($account->uid);
    $this->drupalGet($reset_url);
    $this->assertResponse(403);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
