# user_comment_view()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3580–3591 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3580-L3591)
- **Module/theme:** user
- **Implements:** [hook_comment_view()](../../comment/comment.api.php/hook_comment_view.md)

## Signature

```php
function user_comment_view($comment)
```

## Documentation

```text
Implements hook_comment_view().
```

## Code

```php
function user_comment_view($comment) {
  if (variable_get('user_signatures', 0) && !empty($comment->signature)) {
    // @todo This alters and replaces the original object value, so a
    //   hypothetical process of loading, viewing, and saving will hijack the
    //   stored data. Consider renaming to $comment->signature_safe or similar
    //   here and elsewhere in Drupal 8.
    $comment->signature = check_markup($comment->signature, $comment->signature_format, '', TRUE);
  }
  else {
    $comment->signature = '';
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
