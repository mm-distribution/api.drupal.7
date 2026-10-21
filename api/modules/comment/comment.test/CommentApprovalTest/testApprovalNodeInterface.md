# CommentApprovalTest::testApprovalNodeInterface()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1646–1683 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1646-L1683)
- **Class:** [CommentApprovalTest](../CommentApprovalTest.md)
- **Module/theme:** comment

## Signature

```php
function testApprovalNodeInterface()
```

## Documentation

```text
Test comment approval functionality through node interface.
```

## Code

```php
  function testApprovalNodeInterface() {
    // Set anonymous comments to require approval.
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array(
      'access comments' => TRUE,
      'post comments' => TRUE,
      'skip comment approval' => FALSE,
    ));
    $this->drupalLogin($this->admin_user);
    $this->setCommentAnonymous('0'); // Ensure that doesn't require contact info.
    $this->drupalLogout();

    // Post anonymous comment without contact info.
    $subject = $this->randomName();
    $body = $this->randomName();
    $this->postComment($this->node, $body, $subject, TRUE); // Set $contact to true so that it won't check for id and message.
    $this->assertText(t('Your comment has been queued for review by site administrators and will be published after approval.'), 'Comment requires approval.');

    // Get unapproved comment id.
    $this->drupalLogin($this->admin_user);
    $anonymous_comment4 = $this->getUnapprovedComment($subject);
    $anonymous_comment4 = (object) array('id' => $anonymous_comment4, 'subject' => $subject, 'comment' => $body);
    $this->drupalLogout();

    $this->assertFalse($this->commentExists($anonymous_comment4), 'Anonymous comment was not published.');

    // Approve comment.
    $this->drupalLogin($this->admin_user);
    $this->drupalGet('comment/1/approve');
    $this->assertResponse(403, 'Forged comment approval was denied.');
    $this->drupalGet('comment/1/approve', array('query' => array('token' => 'forged')));
    $this->assertResponse(403, 'Forged comment approval was denied.');
    $this->drupalGet('node/' . $this->node->nid);
    $this->clickLink(t('approve'));
    $this->drupalLogout();

    $this->drupalGet('node/' . $this->node->nid);
    $this->assertTrue($this->commentExists($anonymous_comment4), 'Anonymous comment visible.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
