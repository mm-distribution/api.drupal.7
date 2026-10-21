# UserUserSearchTestCase::testUserSearch()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2747–2802 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2747-L2802)
- **Class:** [UserUserSearchTestCase](../UserUserSearchTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserSearch()
```

## Documentation

_No docblock in source._

## Code

```php
  function testUserSearch() {
    // Verify that a user without 'administer users' permission cannot search
    // for users by email address. Additionally, ensure that the username has a
    // plus sign to ensure searching works with that.
    $user1 = $this->drupalCreateUser(array('access user profiles', 'search content', 'use advanced search'));
    $edit['name'] = 'foo+bar';
    $edit['mail'] = $edit['name'] . '@example.com';
    user_save($user1, $edit);
    $this->drupalLogin($user1);
    $keys = $user1->mail;
    $edit = array('keys' => $keys);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertNoText($keys);
    $this->drupalLogout();

    $user2 = $this->drupalCreateUser(array('administer users', 'access user profiles', 'search content', 'use advanced search'));
    $this->drupalLogin($user2);
    $keys = $user2->mail;
    $edit = array('keys' => $keys);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertText($keys);

    // Verify that wildcard search works.
    $keys = $user1->name;
    $keys = substr($keys, 0, 2) . '*' . substr($keys, 4, 2);
    $edit = array('keys' => $keys);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertText($user1->name, 'Search for username wildcard resulted in user name on page for administrative user.');

    // Verify that wildcard search works for email.
    $keys = $user1->mail;
    $keys = substr($keys, 0, 2) . '*' . substr($keys, 4, 2);
    $edit = array('keys' => $keys);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertText($user1->name, 'Search for email wildcard resulted in user name on page for administrative user.');

    // Create a blocked user.
    $blocked_user = $this->drupalCreateUser();
    $edit = array('status' => 0);
    $blocked_user = user_save($blocked_user, $edit);

    // Verify that users with "administer users" permissions can see blocked
    // accounts in search results.
    $edit = array('keys' => $blocked_user->name);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertText($blocked_user->name, 'Blocked users are listed on the user search results for users with the "administer users" permission.');

    // Verify that users without "administer users" permissions do not see
    // blocked accounts in search results.
    $this->drupalLogin($user1);
    $edit = array('keys' => $blocked_user->name);
    $this->drupalPost('search/user/', $edit, t('Search'));
    $this->assertNoText($blocked_user->name, 'Blocked users are hidden from the user search results.');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
