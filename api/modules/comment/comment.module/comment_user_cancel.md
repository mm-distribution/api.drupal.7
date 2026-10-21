# comment_user_cancel()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1408–1426 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1408-L1426)
- **Module/theme:** comment
- **Implements:** [hook_user_cancel()](../../user/user.api.php/hook_user_cancel.md)

## Signature

```php
function comment_user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements hook_user_cancel().
```

## Code

```php
function comment_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_block_unpublish':
      $comments = comment_load_multiple(array(), array('uid' => $account->uid));
      foreach ($comments as $comment) {
        $comment->status = 0;
        comment_save($comment);
      }
      break;

    case 'user_cancel_reassign':
      $comments = comment_load_multiple(array(), array('uid' => $account->uid));
      foreach ($comments as $comment) {
        $comment->uid = 0;
        comment_save($comment);
      }
      break;
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
