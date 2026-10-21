# CommentInterfaceTest::assertCommentLinks()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 856–942 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L856-L942)
- **Class:** [CommentInterfaceTest](../CommentInterfaceTest.md)
- **Module/theme:** comment

## Signature

```php
function assertCommentLinks(array $info)
```

## Documentation

```text
Asserts that comment links appear according to the passed environment setup.

@param $info
  An associative array describing the environment to pass to
  setEnvironment().
```

## Code

```php
  function assertCommentLinks(array $info) {
    $info = $this->setEnvironment($info);

    $nid = $this->node->nid;

    foreach (array('', "node/$nid") as $path) {
      $this->drupalGet($path);

      // User is allowed to view comments.
      if ($info['access comments']) {
        if ($path == '') {
          // In teaser view, a link containing the comment count is always
          // expected.
          if ($info['comment count']) {
            $this->assertLink(t('1 comment'));

            // For logged in users, a link containing the amount of new/unread
            // comments is expected.
            // See important note about comment_num_new() below.
            if ($this->loggedInUser && isset($this->comment) && !isset($this->comment->seen)) {
              $this->assertLink(t('1 new comment'));
              $this->comment->seen = TRUE;
            }
          }
        }
      }
      else {
        $this->assertNoLink(t('1 comment'));
        $this->assertNoLink(t('1 new comment'));
      }
      // comment_num_new() is based on node views, so comments are marked as
      // read when a node is viewed, regardless of whether we have access to
      // comments.
      if ($path == "node/$nid" && $this->loggedInUser && isset($this->comment)) {
        $this->comment->seen = TRUE;
      }

      // User is not allowed to post comments.
      if (!$info['post comments']) {
        $this->assertNoLink('Add new comment');

        // Anonymous users should see a note to log in or register in case
        // authenticated users are allowed to post comments.
        // @see theme_comment_post_forbidden()
        if (!$this->loggedInUser) {
          if (user_access('post comments', $this->web_user)) {
            // The note depends on whether users are actually able to register.
            if ($info['user_register']) {
              $this->assertText('Log in or register to post comments');
            }
            else {
              $this->assertText('Log in to post comments');
            }
          }
          else {
            $this->assertNoText('Log in or register to post comments');
            $this->assertNoText('Log in to post comments');
          }
        }
      }
      // User is allowed to post comments.
      else {
        $this->assertNoText('Log in or register to post comments');

        // "Add new comment" is always expected, except when there are no
        // comments or if the user cannot see them.
        if ($path == "node/$nid" && $info['form'] == COMMENT_FORM_BELOW && (!$info['comment count'] || !$info['access comments'])) {
          $this->assertNoLink('Add new comment');
        }
        else {
          $this->assertLink('Add new comment');
        }

        // Also verify that the comment form appears according to the configured
        // location.
        if ($path == "node/$nid") {
          $elements = $this->xpath('//form[@id=:id]', array(':id' => 'comment-form'));
          if ($info['form'] == COMMENT_FORM_BELOW) {
            $this->assertTrue(count($elements), 'Comment form found below.');
          }
          else {
            $this->assertFalse(count($elements), 'Comment form not found below.');
          }
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
