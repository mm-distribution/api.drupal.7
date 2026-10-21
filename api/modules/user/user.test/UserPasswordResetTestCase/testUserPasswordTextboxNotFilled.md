# UserPasswordResetTestCase::testUserPasswordTextboxNotFilled()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 832–853 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L832-L853)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPasswordTextboxNotFilled()
```

## Documentation

```text
Tests the text box on incorrect login via link to password reset page.
```

## Code

```php
  function testUserPasswordTextboxNotFilled() {
    $this->drupalGet('user/login');
    $edit = array(
      'name' => $this->randomName(),
      'pass' => $this->randomName(),
    );
    $this->drupalPost('user', $edit, t('Log in'));
    // Verify we don't pass the username as a query parameter.
    $this->assertNoRaw(t('Sorry, unrecognized username or password. <a href="@password">Have you forgotten your password?</a>',
      array('@password' => url('user/password', array('query' => array('name' => $edit['name']))))));
    $this->assertRaw(t('Sorry, unrecognized username or password. <a href="@password">Have you forgotten your password?</a>',
      array('@password' => url('user/password'))));
    unset($edit['pass']);
    // Verify the field is empty by default.
    $this->drupalGet('user/password');
    $this->assertFieldByName('name', '', 'User name not found.');
    // Ensure the name field value is not cached.
    $this->drupalGet('user/password', array('query' => array('name' => $edit['name'])));
    $this->assertFieldByName('name', $edit['name'], 'User name found.');
    $this->drupalGet('user/password');
    $this->assertNoFieldByName('name', $edit['name'], 'User name not found.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
