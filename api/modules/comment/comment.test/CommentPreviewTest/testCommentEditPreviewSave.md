# CommentPreviewTest::testCommentEditPreviewSave()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1007–1075 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1007-L1075)
- **Class:** [CommentPreviewTest](../CommentPreviewTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentEditPreviewSave()
```

## Documentation

```text
Test comment edit, preview, and save.
```

## Code

```php
  function testCommentEditPreviewSave() {
    $langcode = LANGUAGE_NONE;
    $web_user = $this->drupalCreateUser(array('access comments', 'post comments', 'skip comment approval', 'edit own comments'));
    $this->drupalLogin($this->admin_user);
    $this->setCommentPreview(DRUPAL_OPTIONAL);
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Comment paging changed.');

    $edit = array();
    $edit['subject'] = $this->randomName(8);
    $edit['comment_body[' . $langcode . '][0][value]'] = $this->randomName(16);
    $edit['name'] = $web_user->name;
    $edit['date'] = '2008-03-02 17:23 +0300';
    $raw_date = strtotime($edit['date']);
    $expected_text_date = format_date($raw_date);
    $expected_form_date = format_date($raw_date, 'custom', 'Y-m-d H:i:s O');
    $comment = $this->postComment($this->node, $edit['subject'], $edit['comment_body[' . $langcode . '][0][value]'], TRUE);
    $this->drupalPost('comment/' . $comment->id . '/edit', $edit, t('Preview'));

    // Check that the preview is displaying the subject, comment, author and date correctly.
    $this->assertTitle(t('Preview comment | Drupal'), 'Page title is "Preview comment".');
    $this->assertText($edit['subject'], 'Subject displayed.');
    $this->assertText($edit['comment_body[' . $langcode . '][0][value]'], 'Comment displayed.');
    $this->assertText($edit['name'], 'Author displayed.');
    $this->assertText($expected_text_date, 'Date displayed.');

    // Check that the subject, comment, author and date fields are displayed with the correct values.
    $this->assertFieldByName('subject', $edit['subject'], 'Subject field displayed.');
    $this->assertFieldByName('comment_body[' . $langcode . '][0][value]', $edit['comment_body[' . $langcode . '][0][value]'], 'Comment field displayed.');
    $this->assertFieldByName('name', $edit['name'], 'Author field displayed.');
    $this->assertFieldByName('date', $edit['date'], 'Date field displayed.');

    // Check that saving a comment produces a success message.
    $this->drupalPost('comment/' . $comment->id . '/edit', $edit, t('Save'));
    $this->assertText(t('Your comment has been posted.'), 'Comment posted.');

    // Check that the comment fields are correct after loading the saved comment.
    $this->drupalGet('comment/' . $comment->id . '/edit');
    $this->assertFieldByName('subject', $edit['subject'], 'Subject field displayed.');
    $this->assertFieldByName('comment_body[' . $langcode . '][0][value]', $edit['comment_body[' . $langcode . '][0][value]'], 'Comment field displayed.');
    $this->assertFieldByName('name', $edit['name'], 'Author field displayed.');
    $this->assertFieldByName('date', $expected_form_date, 'Date field displayed.');

    // Submit the form using the displayed values.
    $displayed = array();
    $displayed['subject'] = (string) current($this->xpath("//input[@id='edit-subject']/@value"));
    $displayed['comment_body[' . $langcode . '][0][value]'] = (string) current($this->xpath("//textarea[@id='edit-comment-body-" . $langcode . "-0-value']"));
    $displayed['name'] = (string) current($this->xpath("//input[@id='edit-name']/@value"));
    $displayed['date'] = (string) current($this->xpath("//input[@id='edit-date']/@value"));
    $this->drupalPost('comment/' . $comment->id . '/edit', $displayed, t('Save'));

    // Check that the saved comment is still correct.
    $comment_loaded = comment_load($comment->id);
    $this->assertEqual($comment_loaded->subject, $edit['subject'], 'Subject loaded.');
    $this->assertEqual($comment_loaded->comment_body[$langcode][0]['value'], $edit['comment_body[' . $langcode . '][0][value]'], 'Comment body loaded.');
    $this->assertEqual($comment_loaded->name, $edit['name'], 'Name loaded.');
    $this->assertEqual($comment_loaded->created, $raw_date, 'Date loaded.');
    $this->drupalLogout();

    // Check that the date and time of the comment are correct when edited by
    // non-admin users.
    $user_edit = array();
    $expected_created_time = $comment_loaded->created;
    $this->drupalLogin($web_user);
    $this->drupalPost('comment/' . $comment->id . '/edit', $user_edit, t('Save'));
    $comment_loaded = comment_load($comment->id, TRUE);
    $this->assertEqual($comment_loaded->created, $expected_created_time, 'Expected date and time for comment edited.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
