# UserLoginTestCase::assertFailedLogin()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 470–496 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L470-L496)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function assertFailedLogin($account, $flood_trigger = NULL)
```

## Documentation

```text
Make an unsuccessful login attempt.

@param $account
  A user object with name and pass_raw attributes for the login attempt.
@param $flood_trigger
  Whether or not to expect that the flood control mechanism will be
  triggered.
```

## Code

```php
  function assertFailedLogin($account, $flood_trigger = NULL) {
    $edit = array(
      'name' => $account->name,
      'pass' => $account->pass_raw,
    );
    $this->drupalPost('user', $edit, t('Log in'));
    $this->assertNoFieldByXPath("//input[@name='pass' and @value!='']", NULL, 'Password value attribute is blank.');
    if (isset($flood_trigger)) {
      $this->assertResponse(403);
      $user_log = db_query_range('SELECT message FROM {watchdog} WHERE type = :type ORDER BY wid DESC', 0, 1, array(':type' => 'user'))->fetchField();
      $user_flood_test_log = db_query_range('SELECT message FROM {watchdog} WHERE type = :type ORDER BY wid DESC', 0, 1, array(':type' => 'user_flood_test'))->fetchField();
      if ($flood_trigger == 'user') {
        $this->assertRaw(t('Sorry, there have been more than @count failed login attempts for this account. It is temporarily blocked. Try again later or <a href="@url">request a new password</a>.', array('@url' => url('user/password'), '@count' => variable_get('user_failed_login_user_limit', 5))));
        $this->assertEqual('Flood control blocked login attempt for %user from %ip.', $user_log, 'A watchdog message was logged for the login attempt blocked by flood control per user');
        $this->assertEqual('hook_user_flood_control was passed username %username and IP %ip.', $user_flood_test_log, 'hook_user_flood_control was invoked by flood control per user');
      }
      else {
        // No uid, so the limit is IP-based.
        $this->assertRaw(t('Sorry, too many failed login attempts from your IP address. This IP address is temporarily blocked. Try again later or <a href="@url">request a new password</a>.', array('@url' => url('user/password'))));
        $this->assertEqual('Flood control blocked login attempt from %ip.', $user_log, 'A watchdog message was logged for the login attempt blocked by flood control per IP');
        $this->assertEqual('hook_user_flood_control was passed IP %ip.', $user_flood_test_log, 'hook_user_flood_control was invoked by flood control per IP');
      }
    }
    else {
      $this->assertText(t('Sorry, unrecognized username or password. Have you forgotten your password?'));
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
