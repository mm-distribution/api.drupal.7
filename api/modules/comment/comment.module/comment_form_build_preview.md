# comment_form_build_preview()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2071–2075 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2071-L2075)
- **Module/theme:** comment

## Signature

```php
function comment_form_build_preview($form, &$form_state)
```

## Documentation

```text
Build a preview from submitted form values.
```

## Code

```php
function comment_form_build_preview($form, &$form_state) {
  $comment = comment_form_submit_build_comment($form, $form_state);
  $form_state['comment_preview'] = comment_preview($comment);
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
