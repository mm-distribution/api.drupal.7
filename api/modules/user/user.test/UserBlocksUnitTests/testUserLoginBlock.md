# UserBlocksUnitTests::testUserLoginBlock()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2068–2094 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2068-L2094)
- **Class:** [UserBlocksUnitTests](../UserBlocksUnitTests.md)
- **Module/theme:** user

## Signature

```php
function testUserLoginBlock()
```

## Documentation

```text
Test the user login block.
```

## Code

```php
  function testUserLoginBlock() {
    // Create a user with some permission that anonymous users lack.
    $user = $this->drupalCreateUser(array('administer permissions'));

    // Log in using the block.
    $edit = array();
    $edit['name'] = $user->name;
    $edit['pass'] = $user->pass_raw;
    $this->drupalPost('admin/people/permissions', $edit, t('Log in'));
    $this->assertNoText(t('User login'), 'Logged in.');

    // Check that we are still on the same page.
    $this->assertEqual(url('admin/people/permissions', array('absolute' => TRUE)), $this->getUrl(), 'Still on the same page after login for access denied page');

    // Now, log out and repeat with a non-403 page.
    $this->drupalLogout();
    $this->drupalPost('filter/tips', $edit, t('Log in'));
    $this->assertNoText(t('User login'), 'Logged in.');
    $this->assertPattern('!<title.*?' . t('Compose tips') . '.*?</title>!', 'Still on the same page after login for allowed page');

    // Check that the user login block is not vulnerable to information
    // disclosure to third party sites.
    $this->drupalLogout();
    $this->drupalPost('http://example.com/', $edit, t('Log in'), array('external' => FALSE));
    // Check that we remain on the site after login.
    $this->assertEqual(url('user/' . $user->uid, array('absolute' => TRUE)), $this->getUrl(), 'Redirected to user profile page after login from the frontpage');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
