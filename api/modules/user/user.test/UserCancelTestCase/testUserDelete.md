# UserCancelTestCase::testUserDelete()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1224–1281 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1224-L1281)
- **Class:** [UserCancelTestCase](../UserCancelTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserDelete()
```

## Documentation

```text
Delete account and remove all content.
```

## Code

```php
  function testUserDelete() {
    variable_set('user_cancel_method', 'user_cancel_delete');

    // Create a user.
    $account = $this->drupalCreateUser(array('cancel account', 'post comments', 'skip comment approval'));
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);

    // Create a simple node.
    $node = $this->drupalCreateNode(array('uid' => $account->uid));

    // Create comment.
    $langcode = LANGUAGE_NONE;
    $edit = array();
    $edit['subject'] = $this->randomName(8);
    $edit['comment_body[' . $langcode . '][0][value]'] = $this->randomName(16);

    $this->drupalPost('comment/reply/' . $node->nid, $edit, t('Preview'));
    $this->drupalPost(NULL, array(), t('Save'));
    $this->assertText(t('Your comment has been posted.'));
    $comments = comment_load_multiple(array(), array('subject' => $edit['subject']));
    $comment = reset($comments);
    $this->assertTrue($comment->cid, 'Comment found.');

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
    $this->assertText(t('Your account will be removed and all account information deleted. All of your content will also be deleted.'), 'Informs that all content will be deleted.');

    // Confirm account cancellation.
    $timestamp = time();
    $this->drupalPost(NULL, NULL, t('Cancel account'));
    $this->assertText(t('A confirmation request to cancel your account has been sent to your e-mail address.'), 'Account cancellation request mailed message displayed.');

    // Confirm account cancellation request.
    $this->drupalGet("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail));
    $this->assertFalse(user_load($account->uid, TRUE), 'User is not found in the database.');

    // Confirm that user's content has been deleted.
    $this->assertFalse(node_load($node->nid, NULL, TRUE), 'Node of the user has been deleted.');
    $this->assertFalse(node_load($node->nid, $revision, TRUE), 'Node revision of the user has been deleted.');
    $this->assertTrue(node_load($revision_node->nid, NULL, TRUE), "Current revision of the user's node was not deleted.");
    $this->assertFalse(comment_load($comment->cid), 'Comment of the user has been deleted.');

    // Confirm that the confirmation message made it through to the end user.
    $this->assertRaw(t('%name has been deleted.', array('%name' => $account->name)), "Confirmation message displayed to user.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
