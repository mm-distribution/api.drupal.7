# UserBlocksUnitTests::testWhosOnlineBlock()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2099–2129 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2099-L2129)
- **Class:** [UserBlocksUnitTests](../UserBlocksUnitTests.md)
- **Module/theme:** user

## Signature

```php
function testWhosOnlineBlock()
```

## Documentation

```text
Test the Who's Online block.
```

## Code

```php
  function testWhosOnlineBlock() {
    // Generate users and make sure there are no current user sessions.
    $user1 = $this->drupalCreateUser(array());
    $user2 = $this->drupalCreateUser(array());
    $user3 = $this->drupalCreateUser(array());
    $this->assertEqual(db_query("SELECT COUNT(*) FROM {sessions}")->fetchField(), 0, 'Sessions table is empty.');

    // Insert a user with two sessions.
    $this->insertSession(array('uid' => $user1->uid));
    $this->insertSession(array('uid' => $user1->uid));
    $this->assertEqual(db_query("SELECT COUNT(*) FROM {sessions} WHERE uid = :uid", array(':uid' => $user1->uid))->fetchField(), 2, 'Duplicate user session has been inserted.');

    // Insert a user with only one session.
    $this->insertSession(array('uid' => $user2->uid, 'timestamp' => REQUEST_TIME + 1));

    // Insert an inactive logged-in user who should not be seen in the block.
    $this->insertSession(array('uid' => $user3->uid, 'timestamp' => (REQUEST_TIME - variable_get('user_block_seconds_online', 900) - 1)));

    // Insert two anonymous user sessions.
    $this->insertSession();
    $this->insertSession();

    // Test block output.
    $block = user_block_view('online');
    $this->drupalSetContent($block['content']);
    $this->assertRaw(t('2 users'), 'Correct number of online users (2 users).');
    $this->assertText($user1->name, 'Active user 1 found in online list.');
    $this->assertText($user2->name, 'Active user 2 found in online list.');
    $this->assertNoText($user3->name, "Inactive user not found in online list.");
    $this->assertTrue(strpos($this->drupalGetContent(), $user1->name) > strpos($this->drupalGetContent(), $user2->name), 'Online users are ordered correctly.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
