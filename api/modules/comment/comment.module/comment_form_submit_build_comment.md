# comment_form_submit_build_comment()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2243–2248 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2243-L2248)
- **Module/theme:** comment

## Signature

```php
function comment_form_submit_build_comment($form, &$form_state)
```

## Documentation

```text
Updates the form state's comment entity by processing this submission's values.

This is the default builder function for the comment form. It is called
during the "Save" and "Preview" submit handlers to retrieve the entity to
save or preview. This function can also be called by a "Next" button of a
wizard to update the form state's entity with the current step's values
before proceeding to the next step.

@see comment_form()
```

## Code

```php
function comment_form_submit_build_comment($form, &$form_state) {
  $comment = $form_state['comment'];
  entity_form_submit_build_entity('comment', $comment, $form, $form_state);
  comment_submit($comment);
  return $comment;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
