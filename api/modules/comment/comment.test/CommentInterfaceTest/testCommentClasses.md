# CommentInterfaceTest::testCommentClasses()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 483–585 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L483-L585)
- **Class:** [CommentInterfaceTest](../CommentInterfaceTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentClasses()
```

## Documentation

```text
Tests CSS classes on comments.
```

## Code

```php
  function testCommentClasses() {
    // Create all permutations for comments, users, and nodes.
    $parameters = array(
      'node_uid' => array(0, $this->web_user->uid),
      'comment_uid' => array(0, $this->web_user->uid, $this->admin_user->uid),
      'comment_status' => array(COMMENT_PUBLISHED, COMMENT_NOT_PUBLISHED),
      'user' => array('anonymous', 'authenticated', 'admin'),
    );
    $permutations = $this->generatePermutations($parameters);

    foreach ($permutations as $case) {
      // Create a new node.
      $node = $this->drupalCreateNode(array('type' => 'article', 'uid' => $case['node_uid']));

      // Add a comment.
      $comment = (object) array(
        'cid' => NULL,
        'nid' => $node->nid,
        'pid' => 0,
        'uid' => $case['comment_uid'],
        'status' => $case['comment_status'],
        'subject' => $this->randomName(),
        'language' => LANGUAGE_NONE,
        'comment_body' => array(LANGUAGE_NONE => array($this->randomName())),
      );
      comment_save($comment);

      // Adjust the current/viewing user.
      switch ($case['user']) {
        case 'anonymous':
          $this->drupalLogout();
          $case['user_uid'] = 0;
          break;

        case 'authenticated':
          $this->drupalLogin($this->web_user);
          $case['user_uid'] = $this->web_user->uid;
          break;

        case 'admin':
          $this->drupalLogin($this->admin_user);
          $case['user_uid'] = $this->admin_user->uid;
          break;
      }
      // Request the node with the comment.
      $this->drupalGet('node/' . $node->nid);

      // Verify classes if the comment is visible for the current user.
      if ($case['comment_status'] == COMMENT_PUBLISHED || $case['user'] == 'admin') {
        // Verify the comment-by-anonymous class.
        $comments = $this->xpath('//*[contains(@class, "comment-by-anonymous")]');
        if ($case['comment_uid'] == 0) {
          $this->assertTrue(count($comments) == 1, 'comment-by-anonymous class found.');
        }
        else {
          $this->assertFalse(count($comments), 'comment-by-anonymous class not found.');
        }

        // Verify the comment-by-node-author class.
        $comments = $this->xpath('//*[contains(@class, "comment-by-node-author")]');
        if ($case['comment_uid'] > 0 && $case['comment_uid'] == $case['node_uid']) {
          $this->assertTrue(count($comments) == 1, 'comment-by-node-author class found.');
        }
        else {
          $this->assertFalse(count($comments), 'comment-by-node-author class not found.');
        }

        // Verify the comment-by-viewer class.
        $comments = $this->xpath('//*[contains(@class, "comment-by-viewer")]');
        if ($case['comment_uid'] > 0 && $case['comment_uid'] == $case['user_uid']) {
          $this->assertTrue(count($comments) == 1, 'comment-by-viewer class found.');
        }
        else {
          $this->assertFalse(count($comments), 'comment-by-viewer class not found.');
        }
      }

      // Verify the comment-unpublished class.
      $comments = $this->xpath('//*[contains(@class, "comment-unpublished")]');
      if ($case['comment_status'] == COMMENT_NOT_PUBLISHED && $case['user'] == 'admin') {
        $this->assertTrue(count($comments) == 1, 'comment-unpublished class found.');
      }
      else {
        $this->assertFalse(count($comments), 'comment-unpublished class not found.');
      }

      // Verify the comment-new class.
      if ($case['comment_status'] == COMMENT_PUBLISHED || $case['user'] == 'admin') {
        $comments = $this->xpath('//*[contains(@class, "comment-new")]');
        if ($case['user'] != 'anonymous') {
          $this->assertTrue(count($comments) == 1, 'comment-new class found.');

          // Request the node again. The comment-new class should disappear.
          $this->drupalGet('node/' . $node->nid);
          $comments = $this->xpath('//*[contains(@class, "comment-new")]');
          $this->assertFalse(count($comments), 'comment-new class not found.');
        }
        else {
          $this->assertFalse(count($comments), 'comment-new class not found.');
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
