# comment_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2183–2230 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2183-L2230)
- **Module/theme:** comment

## Signature

```php
function comment_submit($comment)
```

## Documentation

```text
Prepare a comment for submission.
```

## Code

```php
function comment_submit($comment) {
  // @todo Legacy support. Remove in Drupal 8.
  if (is_array($comment)) {
    $comment += array('subject' => '');
    $comment = (object) $comment;
  }

  if (empty($comment->date)) {
    $comment->date = 'now';
  }
  $comment->created = strtotime($comment->date, REQUEST_TIME);
  $comment->changed = REQUEST_TIME;

  // If the comment was posted by a registered user, assign the author's ID.
  // @todo Too fragile. Should be prepared and stored in comment_form() already.
  if (!$comment->is_anonymous && !empty($comment->name) && ($account = user_load_by_name($comment->name))) {
    $comment->uid = $account->uid;
  }
  // If the comment was posted by an anonymous user and no author name was
  // required, use "Anonymous" by default.
  if ($comment->is_anonymous && (!isset($comment->name) || $comment->name === '')) {
    $comment->name = variable_get('anonymous', t('Anonymous'));
  }

  // Validate the comment's subject. If not specified, extract from comment body.
  if (trim($comment->subject) == '') {
    // The body may be in any format, so:
    // 1) Filter it into HTML
    // 2) Strip out all HTML tags
    // 3) Convert entities back to plain-text.
    $field = field_info_field('comment_body');
    $langcode = field_is_translatable('comment', $field) ? entity_language('comment', $comment) : LANGUAGE_NONE;
    $comment_body = $comment->comment_body[$langcode][0];
    if (isset($comment_body['format'])) {
      $comment_text = check_markup($comment_body['value'], $comment_body['format']);
    }
    else {
      $comment_text = check_plain($comment_body['value']);
    }
    $comment->subject = truncate_utf8(trim(decode_entities(strip_tags($comment_text))), 29, TRUE);
    // Edge cases where the comment body is populated only by HTML tags will
    // require a default subject.
    if ($comment->subject == '') {
      $comment->subject = t('(No subject)');
    }
  }
  return $comment;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
