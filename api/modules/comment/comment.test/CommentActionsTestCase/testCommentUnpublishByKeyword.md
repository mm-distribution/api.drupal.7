# CommentActionsTestCase::testCommentUnpublishByKeyword()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1999–2029 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1999-L2029)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
public function testCommentUnpublishByKeyword()
```

## Documentation

```text
Tests the unpublish comment by keyword action.
```

## Code

```php
  public function testCommentUnpublishByKeyword() {
    $this->drupalLogin($this->admin_user);
    $callback = 'comment_unpublish_by_keyword_action';
    $hash = drupal_hash_base64($callback);
    $comment_text = $keywords = $this->randomName();
    $edit = array(
      'actions_label' => $callback,
      'keywords' => $keywords,
    );

    $this->drupalPost("admin/config/system/actions/configure/$hash", $edit, t('Save'));

    $action = db_query("SELECT aid, type, callback, parameters, label FROM {actions} WHERE callback = :callback", array(':callback' => $callback))->fetchObject();

    $this->assertTrue($action, 'The action could be loaded.');

    $comment = $this->postComment($this->node, $comment_text, $this->randomName());

    // Load the full comment so that status is available.
    $comment = comment_load($comment->id);

    $this->assertTrue($comment->status == COMMENT_PUBLISHED, 'The comment status was set to published.');

    comment_unpublish_by_keyword_action($comment, array('keywords' => array($keywords)));

    // We need to make sure that the comment has been saved with status
    // unpublished.
    $this->assertEqual(comment_load($comment->cid)->status, COMMENT_NOT_PUBLISHED, 'Comment was unpublished.');
    $this->assertWatchdogMessage('Unpublished comment %subject.', array('%subject' => $comment->subject), 'Found watchdog message.');
    $this->clearWatchdog();
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
