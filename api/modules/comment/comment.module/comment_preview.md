# comment_preview()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2080–2133 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2080-L2133)
- **Module/theme:** comment

## Signature

```php
function comment_preview($comment)
```

## Documentation

```text
Generate a comment preview.
```

## Code

```php
function comment_preview($comment) {
  global $user;

  drupal_set_title(t('Preview comment'), PASS_THROUGH);

  $node = node_load($comment->nid);

  if (!form_get_errors()) {
    $comment_body = field_get_items('comment', $comment, 'comment_body');
    $comment->format = $comment_body[0]['format'];
    // Attach the user and time information.
    if (!empty($comment->name)) {
      $account = user_load_by_name($comment->name);
    }
    elseif ($user->uid && empty($comment->is_anonymous)) {
      $account = $user;
    }

    if (!empty($account->uid)) {
      $comment->uid = $account->uid;
      $comment->name = check_plain($account->name);
      $comment->signature = $account->signature;
      $comment->signature_format = $account->signature_format;
      $comment->picture = $account->picture;
    }
    elseif (empty($comment->name)) {
      $comment->name = variable_get('anonymous', t('Anonymous'));
    }

    $comment->created = !empty($comment->created) ? $comment->created : REQUEST_TIME;
    $comment->changed = REQUEST_TIME;
    $comment->in_preview = TRUE;
    $comment_build = comment_view($comment, $node);
    $comment_build['#weight'] = -100;

    $form['comment_preview'] = $comment_build;
  }

  if ($comment->pid) {
    $build = array();
    if ($comments = comment_load_multiple(array($comment->pid), array('status' => COMMENT_PUBLISHED))) {
      $parent_comment = $comments[$comment->pid];
      $build = comment_view($parent_comment, $node);
    }
  }
  else {
    $build = node_view($node);
  }

  $form['comment_output_below'] = $build;
  $form['comment_output_below']['#weight'] = 100;

  return $form;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
