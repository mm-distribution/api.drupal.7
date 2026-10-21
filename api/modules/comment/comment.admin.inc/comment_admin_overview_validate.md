# comment_admin_overview_validate()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 146–152 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L146-L152)
- **Module/theme:** comment

## Signature

```php
function comment_admin_overview_validate($form, &$form_state)
```

## Documentation

```text
Validate comment_admin_overview form submissions.
```

## Code

```php
function comment_admin_overview_validate($form, &$form_state) {
  $form_state['values']['comments'] = array_diff($form_state['values']['comments'], array(0));
  // We can't execute any 'Update options' if no comments were selected.
  if (count($form_state['values']['comments']) == 0) {
    form_set_error('', t('Select one or more comments to perform the update on.'));
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
