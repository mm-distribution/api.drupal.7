# UserLoginTestCase::testPasswordRehashOnLogin()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 428–448 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L428-L448)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function testPasswordRehashOnLogin()
```

## Documentation

```text
Test that user password is re-hashed upon login after changing $count_log2.
```

## Code

```php
  function testPasswordRehashOnLogin() {
    // Load password hashing API.
    require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
    // Set initial $count_log2 to the default, DRUPAL_HASH_COUNT.
    variable_set('password_count_log2', DRUPAL_HASH_COUNT);
    // Create a new user and authenticate.
    $account = $this->drupalCreateUser(array());
    $password = $account->pass_raw;
    $this->drupalLogin($account);
    $this->drupalLogout();
    // Load the stored user. The password hash should reflect $count_log2.
    $account = user_load($account->uid);
    $this->assertIdentical(_password_get_count_log2($account->pass), DRUPAL_HASH_COUNT);
    // Change $count_log2 and log in again.
    variable_set('password_count_log2', DRUPAL_HASH_COUNT + 1);
    $account->pass_raw = $password;
    $this->drupalLogin($account);
    // Load the stored user, which should have a different password hash now.
    $account = user_load($account->uid, TRUE);
    $this->assertIdentical(_password_get_count_log2($account->pass), DRUPAL_HASH_COUNT + 1);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
