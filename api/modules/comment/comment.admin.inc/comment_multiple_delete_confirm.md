# comment_multiple_delete_confirm()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 195–225 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L195-L225)
- **Module/theme:** comment
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function comment_multiple_delete_confirm($form, &$form_state)
```

## Documentation

```text
List the selected comments and verify that the admin wants to delete them.

@param $form_state
  An associative array containing the current state of the form.
@return
  TRUE if the comments should be deleted, FALSE otherwise.
@ingroup forms
@see comment_multiple_delete_confirm_submit()
```

## Code

```php
function comment_multiple_delete_confirm($form, &$form_state) {
  $edit = $form_state['input'];

  $form['comments'] = array(
    '#prefix' => '<ul>',
    '#suffix' => '</ul>',
    '#tree' => TRUE,
  );
  // array_filter() returns only elements with actual values.
  $comment_counter = 0;
  foreach (array_filter($edit['comments']) as $cid => $value) {
    $comment = comment_load($cid);
    if (is_object($comment) && is_numeric($comment->cid)) {
      $subject = db_query('SELECT subject FROM {comment} WHERE cid = :cid', array(':cid' => $cid))->fetchField();
      $form['comments'][$cid] = array('#type' => 'hidden', '#value' => $cid, '#prefix' => '<li>', '#suffix' => check_plain($subject) . '</li>');
      $comment_counter++;
    }
  }
  $form['operation'] = array('#type' => 'hidden', '#value' => 'delete');

  if (!$comment_counter) {
    drupal_set_message(t('There do not appear to be any comments to delete, or your selected comment was deleted by another administrator.'));
    drupal_goto('admin/content/comment');
  }
  else {
    return confirm_form($form,
                        t('Are you sure you want to delete these comments and all their children?'),
                        'admin/content/comment', t('This action cannot be undone.'),
                        t('Delete comments'), t('Cancel'));
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
