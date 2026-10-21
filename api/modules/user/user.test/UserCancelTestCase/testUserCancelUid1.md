# UserCancelTestCase::testUserCancelUid1()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1017–1047 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1017-L1047)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserCancelUid1()
```

## Documentation

```text
Tests that user account for uid 1 cannot be cancelled.

This should never be possible, or the site owner would become unable to
administer the site.
```

## Code

```php
  function testUserCancelUid1() {
    // Update uid 1's name and password to we know it.
    $password = user_password();
    require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
    $account = array(
      'name' => 'user1',
      'pass' => user_hash_password(trim($password)),
    );
    // We cannot use user_save() here or the password would be hashed again.
    db_update('users')
      ->fields($account)
      ->condition('uid', 1)
      ->execute();

    // Reload and log in uid 1.
    $user1 = user_load(1, TRUE);
    $user1->pass_raw = $password;

    // Try to cancel uid 1's account with a different user.
    $this->admin_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($this->admin_user);
    $edit = array(
      'operation' => 'cancel',
      'accounts[1]' => TRUE,
    );
    $this->drupalPost('admin/people', $edit, t('Update'));

    // Verify that uid 1's account was not cancelled.
    $user1 = user_load(1, TRUE);
    $this->assertEqual($user1->status, 1, 'User #1 still exists and is not blocked.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
