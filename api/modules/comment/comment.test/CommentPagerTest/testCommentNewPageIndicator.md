# CommentPagerTest::testCommentNewPageIndicator()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1419–1493 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1419-L1493)
- **Class:** [CommentPagerTest](../CommentPagerTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentNewPageIndicator()
```

## Documentation

```text
Test comment_new_page_count().
```

## Code

```php
  function testCommentNewPageIndicator() {
    $this->drupalLogin($this->admin_user);

    // Set comment variables.
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentPreview(DRUPAL_DISABLED);

    // Set comments to one per page so that we are able to test paging without
    // needing to insert large numbers of comments.
    $this->setCommentsPerPage(1);

    // Create a node and three comments.
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $comments = array();
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the second comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[1]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the first comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[0]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the last comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[2]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // At this point, the comment tree is:
    // - 0
    //   - 4
    // - 1
    //   - 3
    // - 2
    //   - 5

    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_FLAT, 'Comment paging changed.');

    $expected_pages = array(
      1 => 5, // Page of comment 5
      2 => 4, // Page of comment 4
      3 => 3, // Page of comment 3
      4 => 2, // Page of comment 2
      5 => 1, // Page of comment 1
      6 => 0, // Page of comment 0
    );

    $node = node_load($node->nid);
    foreach ($expected_pages as $new_replies => $expected_page) {
      $returned = comment_new_page_count($node->comment_count, $new_replies, $node);
      $returned_page = is_array($returned) ? $returned['page'] : 0;
      $this->assertIdentical($expected_page, $returned_page, format_string('Flat mode, @new replies: expected page @expected, returned page @returned.', array('@new' => $new_replies, '@expected' => $expected_page, '@returned' => $returned_page)));
    }

    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Switched to threaded mode.');

    $expected_pages = array(
      1 => 5, // Page of comment 5
      2 => 1, // Page of comment 4
      3 => 1, // Page of comment 4
      4 => 1, // Page of comment 4
      5 => 1, // Page of comment 4
      6 => 0, // Page of comment 0
    );

    $node = node_load($node->nid);
    foreach ($expected_pages as $new_replies => $expected_page) {
      $returned = comment_new_page_count($node->comment_count, $new_replies, $node);
      $returned_page = is_array($returned) ? $returned['page'] : 0;
      $this->assertEqual($expected_page, $returned_page, format_string('Threaded mode, @new replies: expected page @expected, returned page @returned.', array('@new' => $new_replies, '@expected' => $expected_page, '@returned' => $returned_page)));
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
