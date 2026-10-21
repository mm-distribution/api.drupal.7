# comment_unpublish_by_keyword_action_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2672–2674 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2672-L2674)
- **Module/theme:** comment

## Signature

```php
function comment_unpublish_by_keyword_action_submit($form, $form_state)
```

## Documentation

```text
Process comment_unpublish_by_keyword_action_form form submissions.

@see comment_unpublish_by_keyword_action()
```

## Code

```php
function comment_unpublish_by_keyword_action_submit($form, $form_state) {
  return array('keywords' => drupal_explode_tags($form_state['values']['keywords']));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
