# UserLoginTestCase::resetUserPassword()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 504–515 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L504-L515)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
protected function resetUserPassword($user)
```

## Documentation

```text
Resets the user password and logs the user in.

@param object $user
  The account to reset the password for.
```

## Code

```php
  protected function resetUserPassword($user) {
    $this->drupalGet('user/password');
    $edit['name'] = $user->name;
    $this->drupalPost(NULL, $edit, 'E-mail new password');
    $emails = $this->drupalGetMails();
    $email = end($emails);
    $urls = array();
    preg_match('#.+user/reset/.+#', $email['body'], $urls);
    $resetURL = $urls[0];
    $this->drupalGet($resetURL);
    $this->drupalPost(NULL, NULL, 'Log in');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
