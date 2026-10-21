# DrupalWebTestCase::drupalLogin()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1357–1375 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1357-L1375)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalLogin(stdClass $account)
```

## Documentation

```text
Log in a user with the internal browser.

If a user is already logged in, then the current user is logged out before
logging in the specified user.

Please note that neither the global $user nor the passed-in user object is
populated with data of the logged in user. If you need full access to the
user object after logging in, it must be updated manually. If you also need
access to the plain-text password of the user (set by drupalCreateUser()),
e.g. to log in the same user again, then it must be re-assigned manually.
For example:
@code
  // Create a user.
  $account = $this->drupalCreateUser(array());
  $this->drupalLogin($account);
  // Load real user object.
  $pass_raw = $account->pass_raw;
  $account = user_load($account->uid);
  $account->pass_raw = $pass_raw;
@endcode

@param $account
  User object representing the user to log in.

@see drupalCreateUser()
```

## Code

```php
  protected function drupalLogin(stdClass $account) {
    if ($this->loggedInUser) {
      $this->drupalLogout();
    }

    $edit = array(
      'name' => $account->name,
      'pass' => $account->pass_raw
    );
    $this->drupalPost('user', $edit, t('Log in'));

    // If a "log out" link appears on the page, it is almost certainly because
    // the login was successful.
    $pass = $this->assertLink(t('Log out'), 0, t('User %name successfully logged in.', array('%name' => $account->name)), t('User login'));

    if ($pass) {
      $this->loggedInUser = $account;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
