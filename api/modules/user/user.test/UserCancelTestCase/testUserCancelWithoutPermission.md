# UserCancelTestCase::testUserCancelWithoutPermission()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 983–1009 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L983-L1009)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserCancelWithoutPermission()
```

## Documentation

```text
Attempt to cancel account without permission.
```

## Code

```php
  function testUserCancelWithoutPermission() {
    variable_set('user_cancel_method', 'user_cancel_reassign');

    // Create a user.
    $account = $this->drupalCreateUser(array());
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);

    // Create a node.
    $node = $this->drupalCreateNode(array('uid' => $account->uid));

    // Attempt to cancel account.
    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->assertNoRaw(t('Cancel account'), 'No cancel account button displayed.');

    // Attempt bogus account cancellation request confirmation.
    $timestamp = $account->login;
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $this->assertResponse(403, 'Bogus cancelling request rejected.');
    $account = user_load($account->uid);
    $this->assertTrue($account->status == 1, 'User account was not canceled.');

    // Confirm user's content has not been altered.
    $test_node = node_load($node->nid, NULL, TRUE);
    $this->assertTrue(($test_node->uid == $account->uid && $test_node->status == 1), 'Node of the user has not been altered.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
