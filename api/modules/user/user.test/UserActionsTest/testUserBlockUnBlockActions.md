# UserActionsTest::testUserBlockUnBlockActions()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 3023–3064 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L3023-L3064)
- **Class:** [UserActionsTest](../UserActionsTest.md)
- **Module/theme:** user

## Signature

```php
function testUserBlockUnBlockActions()
```

## Documentation

```text
Tests user block and unblock actions.
```

## Code

```php
  function testUserBlockUnBlockActions() {
    $unblocked_user = $this->drupalCreateUser();

    db_truncate('watchdog')->execute();

    // Block a user.
    user_block_user_action($unblocked_user);

    $blocked_user = user_load($unblocked_user->uid, TRUE);
    $this->assertEqual($blocked_user->status, 0, 'User is blocked');

    // Assert that a watchdog message was logged.
    $status = (bool) db_query_range('SELECT 1 FROM {watchdog} WHERE message = :message AND variables = :variables', 0, 1, array(':message' => 'Blocked user %name.', ':variables' => serialize(array('%name' => $blocked_user->name))))->fetchField();
    $this->assert($status, 'A watchdog message was logged by user block action.');

    // Unblock a user.
    user_unblock_user_action($blocked_user);

    $unblocked_user = user_load($unblocked_user->uid, TRUE);
    $this->assertEqual($unblocked_user->status, 1, 'User is unblocked');

    // Assert that a watchdog message was logged.
    $status = (bool) db_query_range('SELECT 1 FROM {watchdog} WHERE message = :message AND variables = :variables', 0, 1, array(':message' => 'Unblocked user %name.', ':variables' => serialize(array('%name' => $unblocked_user->name))))->fetchField();
    $this->assert($status, 'A watchdog message was logged by user unblock action.');

    // Try to unblock the anonymous user.
    db_truncate('watchdog')->execute();
    $anonymous_user = user_load(0);

    // Assert anonymous user is blocked.
    $this->assertEqual($anonymous_user->status, 0, 'Anonymous user is blocked');

    user_unblock_user_action($anonymous_user);

    // Assert anonymous user remains blocked.
    $anonymous_user = user_load(0, TRUE);
    $this->assertEqual($anonymous_user->status, 0, 'Anonymous user remains blocked');

    // Assert that a watchdog message was logged.
    $status = (bool) db_query_range('SELECT 1 FROM {watchdog} WHERE message = :message', 0, 1, array(':message' => 'Anonymous user should not be unblocked.'))->fetchField();
    $this->assert($status, 'A watchdog message was logged by user unblock action.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
