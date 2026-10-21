# UserCancelTestCase::testUserCancelInvalid()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1052–1089 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1052-L1089)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserCancelInvalid()
```

## Documentation

```text
Attempt invalid account cancellations.
```

## Code

```php
  function testUserCancelInvalid() {
    variable_set('user_cancel_method', 'user_cancel_reassign');

    // Create a user.
    $account = $this->drupalCreateUser(array('cancel account'));
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);

    // Create a node.
    $node = $this->drupalCreateNode(array('uid' => $account->uid));

    // Attempt to cancel account.
    $this->drupalPost('user/' . $account->uid . '/edit', NULL, t('Cancel account'));

    // Confirm account cancellation.
    $timestamp = time();
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');

    // Attempt bogus account cancellation request confirmation.
    $bogus_timestamp = $timestamp + 60;
    $this->drupalGet("user/$account->uid/cancel/confirm/$bogus_timestamp/" . user_pass_rehash($account->pass, $bogus_timestamp, $account->login, $account->uid, $account->mail));
    $this->assertText(t('You have tried to use an account cancellation link that has expired. Please request a new one using the form below.'), 'Bogus cancelling request rejected.');
    $account = user_load($account->uid);
    $this->assertTrue($account->status == 1, 'User account was not canceled.');

    // Attempt expired account cancellation request confirmation.
    $bogus_timestamp = $timestamp - 86400 - 60;
    $this->drupalGet("user/$account->uid/cancel/confirm/$bogus_timestamp/" . user_pass_rehash($account->pass, $bogus_timestamp, $account->login, $account->uid, $account->mail));
    $this->assertText(t('You have tried to use an account cancellation link that has expired. Please request a new one using the form below.'), 'Expired cancel account request rejected.');
    $accounts = user_load_multiple(array($account->uid), array('status' => 1));
    $this->assertTrue(reset($accounts), 'User account was not canceled.');

    // Confirm user's content has not been altered.
    $test_node = node_load($node->nid, NULL, TRUE);
    $this->assertTrue(($test_node->uid == $account->uid && $test_node->status == 1), 'Node of the user has not been altered.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
