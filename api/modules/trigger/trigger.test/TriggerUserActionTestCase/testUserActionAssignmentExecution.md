# TriggerUserActionTestCase::testUserActionAssignmentExecution()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 503–541 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L503-L541)
- **Class:** [TriggerUserActionTestCase](../TriggerUserActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testUserActionAssignmentExecution()
```

## Documentation

```text
Tests user action assignment and execution.
```

## Code

```php
  function testUserActionAssignmentExecution() {
    $test_user = $this->drupalCreateUser(array('administer actions', 'create article content', 'access comments', 'administer comments', 'skip comment approval', 'edit own comments'));
    $this->drupalLogin($test_user);

    $triggers = array('comment_presave', 'comment_insert', 'comment_update');
    // system_block_ip_action is difficult to test without ruining the test.
    $actions = array('user_block_user_action');
    foreach ($triggers as $trigger) {
      foreach ($actions as $action) {
        $this->assignSimpleAction($trigger, $action);
      }
    }

    $node = $this->drupalCreateNode(array('type' => 'article'));
    $this->drupalPost("node/{$node->nid}", array('comment_body[und][0][value]' => t("my comment"), 'subject' => t("my comment subject")), t('Save'));
    // Posting a comment should have blocked this user.
    $account = user_load($test_user->uid, TRUE);
    $this->assertTrue($account->status == 0, 'Account is blocked');
    $comment_author_uid = $account->uid;
    // Now rehabilitate the comment author so it can be be blocked again when
    // the comment is updated.
    user_save($account, array('status' => TRUE));

    $test_user = $this->drupalCreateUser(array('administer actions', 'create article content', 'access comments', 'administer comments', 'skip comment approval', 'edit own comments'));
    $this->drupalLogin($test_user);

    // Our original comment will have been comment 1.
    $this->drupalPost("comment/1/edit", array('comment_body[und][0][value]' => t("my comment, updated"), 'subject' => t("my comment subject")), t('Save'));
    $comment_author_account = user_load($comment_author_uid, TRUE);
    $this->assertTrue($comment_author_account->status == 0, format_string('Comment author account (uid=@uid) is blocked after update to comment', array('@uid' => $comment_author_uid)));

    // Verify that the comment was updated.
    $test_user = $this->drupalCreateUser(array('administer actions', 'create article content', 'access comments', 'administer comments', 'skip comment approval', 'edit own comments'));
    $this->drupalLogin($test_user);

    $this->drupalGet("node/$node->nid");
    $this->assertText(t("my comment, updated"));
    $this->verboseEmail();
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
