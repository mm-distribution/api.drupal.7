# CommentBlockFunctionalTest::testRecentCommentBlock()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1701–1775 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1701-L1775)
- **Class:** [CommentBlockFunctionalTest](../CommentBlockFunctionalTest.md)
- **Module/theme:** comment

## Signature

```php
function testRecentCommentBlock()
```

## Documentation

```text
Test the recent comments block.
```

## Code

```php
  function testRecentCommentBlock() {
    $this->drupalLogin($this->admin_user);

    // Set the block to a region to confirm block is available.
    $edit = array(
      'blocks[comment_recent][region]' => 'sidebar_first',
    );
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block saved to first sidebar region.');

    // Set block title and variables.
    $block = array(
      'title' => $this->randomName(),
      'comment_block_count' => 2,
    );
    $this->drupalPost('admin/structure/block/manage/comment/recent/configure', $block, t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block saved.');

    // Add some test comments, one without a subject.
    $comment1 = $this->postComment($this->node, $this->randomName(), $this->randomName());
    $comment2 = $this->postComment($this->node, $this->randomName(), $this->randomName());
    $comment3 = $this->postComment($this->node, $this->randomName());

    // Test that a user without the 'access comments' permission cannot see the
    // block.
    $this->drupalLogout();
    user_role_revoke_permissions(DRUPAL_ANONYMOUS_RID, array('access comments'));
    $this->drupalGet('');
    $this->assertNoText($block['title'], 'Block was not found.');
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access comments'));

    // Test that a user with the 'access comments' permission can see the
    // block.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('');
    $this->assertText($block['title'], 'Block was found.');

    // Test the only the 2 latest comments are shown and in the proper order.
    $this->assertNoText($comment1->subject, 'Comment not found in block.');
    $this->assertText($comment2->subject, 'Comment found in block.');
    $this->assertText($comment3->comment, 'Comment found in block.');
    $this->assertTrue(strpos($this->drupalGetContent(), $comment3->comment) < strpos($this->drupalGetContent(), $comment2->subject), 'Comments were ordered correctly in block.');

    // Set the number of recent comments to show to 10.
    $this->drupalLogout();
    $this->drupalLogin($this->admin_user);
    $block = array(
      'comment_block_count' => 10,
    );
    $this->drupalPost('admin/structure/block/manage/comment/recent/configure', $block, t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block saved.');

    // Post an additional comment.
    $comment4 = $this->postComment($this->node, $this->randomName(), $this->randomName());

    // Test that all four comments are shown.
    $this->assertText($comment1->subject, 'Comment found in block.');
    $this->assertText($comment2->subject, 'Comment found in block.');
    $this->assertText($comment3->comment, 'Comment found in block.');
    $this->assertText($comment4->subject, 'Comment found in block.');

    // Test that links to comments work when comments are across pages.
    $this->setCommentsPerPage(1);
    $this->drupalGet('');
    $this->clickLink($comment1->subject);
    $this->assertText($comment1->subject, 'Comment link goes to correct page.');
    $this->drupalGet('');
    $this->clickLink($comment2->subject);
    $this->assertText($comment2->subject, 'Comment link goes to correct page.');
    $this->clickLink($comment4->subject);
    $this->assertText($comment4->subject, 'Comment link goes to correct page.');
    // Check that when viewing a comment page from a link to the comment, that
    // rel="canonical" is added to the head of the document.
    $this->assertRaw('<link rel="canonical"', 'Canonical URL was found in the HTML head');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
