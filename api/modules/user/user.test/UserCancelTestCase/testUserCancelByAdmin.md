# UserCancelTestCase::testUserCancelByAdmin()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1286–1306 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1286-L1306)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserCancelByAdmin()
```

## Documentation

```text
Create an administrative user and delete another user.
```

## Code

```php
  function testUserCancelByAdmin() {
    variable_set('user_cancel_method', 'user_cancel_reassign');

    // Create a regular user.
    $account = $this->drupalCreateUser(array());

    // Create administrative user.
    $admin_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($admin_user);

    // Delete regular user.
    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertRaw(t('Are you sure you want to cancel the account %name?', array('%name' => $account->name)), 'Confirmation form to cancel account displayed.');
    $this->assertText(t('Select the method to cancel the account above.'), 'Allows to select account cancellation method.');

    // Confirm deletion.
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertRaw(t('%name has been deleted.', array('%name' => $account->name)), 'User deleted.');
    $this->assertFalse(user_load($account->uid), 'User is not found in the database.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
