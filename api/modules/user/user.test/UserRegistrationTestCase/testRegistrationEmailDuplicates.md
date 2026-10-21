# UserRegistrationTestCase::testRegistrationEmailDuplicates()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 111–134 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L111-L134)
- **Class:** [UserRegistrationTestCase](../UserRegistrationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRegistrationEmailDuplicates()
```

## Documentation

_No docblock in source._

## Code

```php
  function testRegistrationEmailDuplicates() {
    // Don't require e-mail verification.
    variable_set('user_email_verification', FALSE);

    // Allow registration by site visitors without administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS);

    // Set up a user to check for duplicates.
    $duplicate_user = $this->drupalCreateUser();

    $edit = array();
    $edit['name'] = $this->randomName();
    $edit['mail'] = $duplicate_user->mail;

    // Attempt to create a new account using an existing e-mail address.
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $this->assertText(t('The e-mail address @email is already registered.', array('@email' => $duplicate_user->mail)), 'Supplying an exact duplicate email address displays an error message');

    // Attempt to bypass duplicate email registration validation by adding spaces.
    $edit['mail'] = '   ' . $duplicate_user->mail . '   ';

    $this->drupalPost('user/register', $edit, t('Create new account'));
    $this->assertText(t('The e-mail address @email is already registered.', array('@email' => $duplicate_user->mail)), 'Supplying a duplicate email address with added whitespace displays an error message');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
