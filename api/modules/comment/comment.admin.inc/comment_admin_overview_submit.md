# comment_admin_overview_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 160–183 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L160-L183)
- **Module/theme:** comment

## Signature

```php
function comment_admin_overview_submit($form, &$form_state)
```

## Documentation

```text
Process comment_admin_overview form submissions.

Execute the chosen 'Update option' on the selected comments, such as
publishing, unpublishing or deleting.
```

## Code

```php
function comment_admin_overview_submit($form, &$form_state) {
  $operation = $form_state['values']['operation'];
  $cids = $form_state['values']['comments'];

  if ($operation == 'delete') {
    comment_delete_multiple($cids);
  }
  else {
    foreach ($cids as $cid => $value) {
      $comment = comment_load($value);

      if ($operation == 'unpublish') {
        $comment->status = COMMENT_NOT_PUBLISHED;
      }
      elseif ($operation == 'publish') {
        $comment->status = COMMENT_PUBLISHED;
      }
      comment_save($comment);
    }
  }
  drupal_set_message(t('The update has been performed.'));
  $form_state['redirect'] = 'admin/content/comment';
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
