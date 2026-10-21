# UserRegistrationTestCase::testRegistrationDefaultValues()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 136–170 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L136-L170)
- **Class:** [UserRegistrationTestCase](../UserRegistrationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRegistrationDefaultValues()
```

## Documentation

_No docblock in source._

## Code

```php
  function testRegistrationDefaultValues() {
    // Allow registration by site visitors without administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS);

    // Don't require e-mail verification.
    variable_set('user_email_verification', FALSE);

    // Set the default timezone to Brussels.
    variable_set('configurable_timezones', 1);
    variable_set('date_default_timezone', 'Europe/Brussels');

    $this->drupalGet('user/register');

    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';
    $edit['pass[pass1]'] = $new_pass = $this->randomName();
    $edit['pass[pass2]'] = $new_pass;
    $this->drupalPost(NULL, $edit, t('Create new account'));

    // Check user fields.
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $this->assertEqual($new_user->name, $name, 'Username matches.');
    $this->assertEqual($new_user->mail, $mail, 'E-mail address matches.');
    $this->assertEqual($new_user->theme, '', 'Correct theme field.');
    $this->assertEqual($new_user->signature, '', 'Correct signature field.');
    $this->assertTrue(($new_user->created > REQUEST_TIME - 20 ), 'Correct creation time.');
    $this->assertEqual($new_user->changed,  $new_user->created, 'Correct changed time.');
    $this->assertEqual($new_user->status, variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) == USER_REGISTER_VISITORS ? 1 : 0, 'Correct status field.');
    $this->assertEqual($new_user->timezone, variable_get('date_default_timezone'), 'Correct time zone field.');
    $this->assertEqual($new_user->language, '', 'Correct language field.');
    $this->assertEqual($new_user->picture, '', 'Correct picture field.');
    $this->assertEqual($new_user->init, $mail, 'Correct init field.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
