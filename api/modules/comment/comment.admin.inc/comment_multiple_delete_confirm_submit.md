# comment_multiple_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 230–239 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L230-L239)
- **Module/theme:** comment

## Signature

```php
function comment_multiple_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Process comment_multiple_delete_confirm form submissions.
```

## Code

```php
function comment_multiple_delete_confirm_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    comment_delete_multiple(array_keys($form_state['values']['comments']));
    cache_clear_all();
    $count = count($form_state['values']['comments']);
    watchdog('content', 'Deleted @count comments.', array('@count' => $count));
    drupal_set_message(format_plural($count, 'Deleted 1 comment.', 'Deleted @count comments.'));
  }
  $form_state['redirect'] = 'admin/content/comment';
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
