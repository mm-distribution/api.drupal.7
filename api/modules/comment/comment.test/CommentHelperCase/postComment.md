# CommentHelperCase::postComment()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 42–100 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L42-L100)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function postComment($node, $comment, $subject = '', $contact = NULL)
```

## Documentation

```text
Post comment.

@param $node
  Node to post comment on.
@param $comment
  Comment body.
@param $subject
  Comment subject.
@param $contact
  Set to NULL for no contact info, TRUE to ignore success checking, and
  array of values to set contact info.
```

## Code

```php
  function postComment($node, $comment, $subject = '', $contact = NULL) {
    $langcode = LANGUAGE_NONE;
    $edit = array();
    $edit['comment_body[' . $langcode . '][0][value]'] = $comment;

    $preview_mode = variable_get('comment_preview_article', DRUPAL_OPTIONAL);
    $subject_mode = variable_get('comment_subject_field_article', 1);

    // Must get the page before we test for fields.
    if ($node !== NULL) {
      $this->drupalGet('comment/reply/' . $node->nid);
    }

    if ($subject_mode == TRUE) {
      $edit['subject'] = $subject;
    }
    else {
      $this->assertNoFieldByName('subject', '', 'Subject field not found.');
    }

    if ($contact !== NULL && is_array($contact)) {
      $edit += $contact;
    }
    switch ($preview_mode) {
      case DRUPAL_REQUIRED:
        // Preview required so no save button should be found.
        $this->assertNoFieldByName('op', t('Save'), 'Save button not found.');
        $this->drupalPost(NULL, $edit, t('Preview'));
        // Don't break here so that we can test post-preview field presence and
        // function below.
      case DRUPAL_OPTIONAL:
        $this->assertFieldByName('op', t('Preview'), 'Preview button found.');
        $this->assertFieldByName('op', t('Save'), 'Save button found.');
        $this->drupalPost(NULL, $edit, t('Save'));
        break;

      case DRUPAL_DISABLED:
        $this->assertNoFieldByName('op', t('Preview'), 'Preview button not found.');
        $this->assertFieldByName('op', t('Save'), 'Save button found.');
        $this->drupalPost(NULL, $edit, t('Save'));
        break;
    }
    $match = array();
    // Get comment ID
    preg_match('/#comment-([0-9]+)/', $this->getURL(), $match);

    // Get comment.
    if ($contact !== TRUE) { // If true then attempting to find error message.
      if ($subject) {
        $this->assertText($subject, 'Comment subject posted.');
      }
      $this->assertText($comment, 'Comment body posted.');
      $this->assertTrue((!empty($match) && !empty($match[1])), 'Comment id found.');
    }

    if (isset($match[1])) {
      return (object) array('id' => $match[1], 'subject' => $subject, 'comment' => $comment);
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
