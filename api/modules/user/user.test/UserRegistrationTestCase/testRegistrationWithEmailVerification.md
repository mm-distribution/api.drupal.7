# UserRegistrationTestCase::testRegistrationWithEmailVerification()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 21–50 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L21-L50)
- **Class:** [UserRegistrationTestCase](../UserRegistrationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRegistrationWithEmailVerification()
```

## Documentation

_No docblock in source._

## Code

```php
  function testRegistrationWithEmailVerification() {
    // Require e-mail verification.
    variable_set('user_email_verification', TRUE);

    // Set registration to administrator only.
    variable_set('user_register', USER_REGISTER_ADMINISTRATORS_ONLY);
    $this->drupalGet('user/register');
    $this->assertResponse(403, 'Registration page is inaccessible when only administrators can create accounts.');

    // Allow registration by site visitors without administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS);
    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $this->assertText(t('A welcome message with further instructions has been sent to your e-mail address.'), 'User registered successfully.');
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $this->assertTrue($new_user->status, 'New account is active after registration.');

    // Allow registration by site visitors, but require administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL);
    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $this->assertFalse($new_user->status, 'New account is blocked until approved by an administrator.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
