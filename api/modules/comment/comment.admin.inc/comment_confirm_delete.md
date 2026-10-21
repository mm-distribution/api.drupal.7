# comment_confirm_delete()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 257–269 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L257-L269)
- **Module/theme:** comment
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function comment_confirm_delete($form, &$form_state, $comment)
```

## Documentation

```text
Form builder; Builds the confirmation form for deleting a single comment.

@ingroup forms
@see comment_confirm_delete_submit()
```

## Code

```php
function comment_confirm_delete($form, &$form_state, $comment) {
  $form['#comment'] = $comment;
  // Always provide entity id in the same form key as in the entity edit form.
  $form['cid'] = array('#type' => 'value', '#value' => $comment->cid);
  return confirm_form(
    $form,
    t('Are you sure you want to delete the comment %title?', array('%title' => $comment->subject)),
    'node/' . $comment->nid,
    t('Any replies to this comment will be lost. This action cannot be undone.'),
    t('Delete'),
    t('Cancel'),
    'comment_confirm_delete');
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
