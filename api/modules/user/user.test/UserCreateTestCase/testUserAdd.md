# UserCreateTestCase::testUserAdd()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2208–2247 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2208-L2247)
- **Class:** [UserCreateTestCase](../UserCreateTestCase.md)
- **Module/theme:** user

## Signature

```php
protected function testUserAdd()
```

## Documentation

```text
Create a user through the administration interface and ensure that it
displays in the user list.
```

## Code

```php
  protected function testUserAdd() {
    $user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($user);

    foreach (array(FALSE, TRUE) as $notify) {
      $edit = array(
        'name' => $this->randomName(),
        'mail' => $this->randomName() . '@example.com',
        'pass[pass1]' => $pass = $this->randomString(),
        'pass[pass2]' => $pass,
        'notify' => $notify,
      );
      $this->drupalPost('admin/people/create', $edit, t('Create new account'));

      if ($notify) {
        $this->assertText(t('A welcome message with further instructions has been e-mailed to the new user @name.', array('@name' => $edit['name'])), 'User created');
        $this->assertEqual(count($this->drupalGetMails()), 1, 'Notification e-mail sent');
      }
      else {
        $this->assertText(t('Created a new user account for @name. No e-mail has been sent.', array('@name' => $edit['name'])), 'User created');
        $this->assertEqual(count($this->drupalGetMails()), 0, 'Notification e-mail not sent');
      }

      $this->drupalGet('admin/people');
      $this->assertText($edit['name'], 'User found in list of users');
    }

    // Test that the password '0' is considered a password.
    $name = $this->randomName();
    $edit = array(
      'name' => $name,
      'mail' => $name . '@example.com',
      'pass[pass1]' => 0,
      'pass[pass2]' => 0,
      'notify' => FALSE,
    );
    $this->drupalPost('admin/people/create', $edit, t('Create new account'));
    $this->assertText(t('Created a new user account for @name. No e-mail has been sent.', array('@name' => $edit['name'])), 'User created with password 0');
    $this->assertNoText('Password field is required');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
