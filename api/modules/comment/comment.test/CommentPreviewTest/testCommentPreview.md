# CommentPreviewTest::testCommentPreview()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 960–1002 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L960-L1002)
- **Class:** [CommentPreviewTest](../CommentPreviewTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentPreview()
```

## Documentation

```text
Test comment preview.
```

## Code

```php
  function testCommentPreview() {
    $langcode = LANGUAGE_NONE;

    // As admin user, configure comment settings.
    $this->drupalLogin($this->admin_user);
    $this->setCommentPreview(DRUPAL_OPTIONAL);
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Comment paging changed.');
    $this->drupalLogout();

    // Login as web user and add a signature and a user picture.
    $this->drupalLogin($this->web_user);
    variable_set('user_signatures', 1);
    variable_set('user_pictures', 1);
    $test_signature = $this->randomName();
    $edit['signature[value]'] = '<a href="http://example.com/">' . $test_signature. '</a>';
    $edit['signature[format]'] = 'filtered_html';
    $image = current($this->drupalGetTestFiles('image'));
    $edit['files[picture_upload]'] = drupal_realpath($image->uri);
    $this->drupalPost('user/' . $this->web_user->uid . '/edit', $edit, t('Save'));

    // As the web user, fill in the comment form and preview the comment.
    $edit = array();
    $edit['subject'] = $this->randomName(8);
    $edit['comment_body[' . $langcode . '][0][value]'] = $this->randomName(16);
    $this->drupalPost('node/' . $this->node->nid, $edit, t('Preview'));

    // Check that the preview is displaying the title and body.
    $this->assertTitle(t('Preview comment | Drupal'), 'Page title is "Preview comment".');
    $this->assertText($edit['subject'], 'Subject displayed.');
    $this->assertText($edit['comment_body[' . $langcode . '][0][value]'], 'Comment displayed.');

    // Check that the title and body fields are displayed with the correct values.
    $this->assertFieldByName('subject', $edit['subject'], 'Subject field displayed.');
    $this->assertFieldByName('comment_body[' . $langcode . '][0][value]', $edit['comment_body[' . $langcode . '][0][value]'], 'Comment field displayed.');

    // Check that the signature is displaying with the correct text format.
    $this->assertLink($test_signature);

    // Check that the user picture is displayed.
    $this->assertFieldByXPath("//div[contains(@class, 'comment-preview')]//div[contains(@class, 'user-picture')]//img", NULL, 'User picture displayed.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
