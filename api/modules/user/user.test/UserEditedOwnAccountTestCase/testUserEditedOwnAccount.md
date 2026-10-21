# UserEditedOwnAccountTestCase::testUserEditedOwnAccount()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2532–2552 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2532-L2552)
- **Class:** [UserEditedOwnAccountTestCase](../UserEditedOwnAccountTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserEditedOwnAccount()
```

## Documentation

_No docblock in source._

## Code

```php
  function testUserEditedOwnAccount() {
    // Change account setting 'Who can register accounts?' to Administrators
    // only.
    variable_set('user_register', USER_REGISTER_ADMINISTRATORS_ONLY);

    // Create a new user account and log in.
    $account = $this->drupalCreateUser(array('change own username'));
    $this->drupalLogin($account);

    // Change own username.
    $edit = array();
    $edit['name'] = $this->randomName();
    $this->drupalPost('user/' . $account->uid . '/edit', $edit, t('Save'));

    // Log out.
    $this->drupalLogout();

    // Set the new name on the user account and attempt to log back in.
    $account->name = $edit['name'];
    $this->drupalLogin($account);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
