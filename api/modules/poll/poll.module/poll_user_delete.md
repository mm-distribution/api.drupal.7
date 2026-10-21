# poll_user_delete()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 992–996 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L992-L996)
- **Module/theme:** poll
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function poll_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function poll_user_delete($account) {
  db_delete('poll_vote')
    ->condition('uid', $account->uid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
