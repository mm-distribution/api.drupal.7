# comment_user_delete()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1431–1434 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1431-L1434)
- **Module/theme:** comment
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function comment_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function comment_user_delete($account) {
  $cids = db_query('SELECT c.cid FROM {comment} c WHERE uid = :uid', array(':uid' => $account->uid))->fetchCol();
  comment_delete_multiple($cids);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
