# UserCancelTestCase::testUserAnonymize()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1173–1219 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1173-L1219)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserAnonymize()
```

## Documentation

```text
Delete account and anonymize all content.
```

## Code

```php
  function testUserAnonymize() {
    variable_set('user_cancel_method', 'user_cancel_reassign');

    // Create a user.
    $account = $this->drupalCreateUser(array('cancel account'));
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);

    // Create a simple node.
    $node = $this->drupalCreateNode(array('uid' => $account->uid));

    // Create a node with two revisions, the initial one belonging to the
    // cancelling user.
    $revision_node = $this->drupalCreateNode(array('uid' => $account->uid));
    $revision = $revision_node->vid;
    $settings = get_object_vars($revision_node);
    $settings['revision'] = 1;
    $settings['uid'] = 1; // Set new/current revision to someone else.
    $revision_node = $this->drupalCreateNode($settings);

    // Attempt to cancel account.
    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('Are you sure you want to cancel your account?'), 'Confirmation form to cancel account displayed.');
    $this->assertRaw(t('Your account will be removed and all account information deleted. All of your content will be assigned to the %anonymous-name user.', array('%anonymous-name' => variable_get('anonymous', t('Anonymous')))), 'Informs that all content will be attributed to anonymous account.');

    // Confirm account cancellation.
    $timestamp = time();
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');

    // Confirm account cancellation request.
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $this->assertFalse(user_load($account->uid, TRUE), 'User is not found in the database.');

    // Confirm that user's content has been attributed to anonymous user.
    $test_node = node_load($node->nid, NULL, TRUE);
    $this->assertTrue(($test_node->uid == 0 && $test_node->status == 1), 'Node of the user has been attributed to anonymous user.');
    $test_node = node_load($revision_node->nid, $revision, TRUE);
    $this->assertTrue(($test_node->revision_uid == 0 && $test_node->status == 1), 'Node revision of the user has been attributed to anonymous user.');
    $test_node = node_load($revision_node->nid, NULL, TRUE);
    $this->assertTrue(($test_node->uid != 0 && $test_node->status == 1), "Current revision of the user's node was not attributed to anonymous user.");

    // Confirm that the confirmation message made it through to the end user.
    $this->assertRaw(t('%name has been deleted.', array('%name' => $account->name)), "Confirmation message displayed to user.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
