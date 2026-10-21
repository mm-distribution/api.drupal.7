# UserCancelTestCase::testUserBlockUnpublish()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1129–1168 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1129-L1168)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserBlockUnpublish()
```

## Documentation

```text
Disable account and unpublish all content.
```

## Code

```php
  function testUserBlockUnpublish() {
    variable_set('user_cancel_method', 'user_cancel_block_unpublish');

    // Create a user.
    $account = $this->drupalCreateUser(array('cancel account'));
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);

    // Create a node with two revisions.
    $node = $this->drupalCreateNode(array('uid' => $account->uid));
    $settings = get_object_vars($node);
    $settings['revision'] = 1;
    $node = $this->drupalCreateNode($settings);

    // Attempt to cancel account.
    $this->drupalGet('user/' . $account->uid . '/edit');
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('Are you sure you want to cancel your account?'), 'Confirmation form to cancel account displayed.');
    $this->assertText(t('Your account will be blocked and you will no longer be able to log in. All of your content will be hidden from everyone but administrators.'), 'Informs that all content will be unpublished.');

    // Confirm account cancellation.
    $timestamp = time();
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');

    // Confirm account cancellation request.
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $account = user_load($account->uid, TRUE);
    $this->assertTrue($account->status == 0, 'User has been blocked.');

    // Confirm user's content has been unpublished.
    $test_node = node_load($node->nid, NULL, TRUE);
    $this->assertTrue($test_node->status == 0, 'Node of the user has been unpublished.');
    $test_node = node_load($node->nid, $node->vid, TRUE);
    $this->assertTrue($test_node->status == 0, 'Node revision of the user has been unpublished.');

    // Confirm that the confirmation message made it through to the end user.
    $this->assertRaw(t('%name has been disabled.', array('%name' => $account->name)), "Confirmation message displayed to user.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
