# poll_user_cancel()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 978–987 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L978-L987)
- **Module/theme:** poll
- **Implements:** [hook_user_cancel()](../../user/user.api.php/hook_user_cancel.md)

## Signature

```php
function poll_user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements hook_user_cancel().
```

## Code

```php
function poll_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_reassign':
      db_update('poll_vote')
        ->fields(array('uid' => 0))
        ->condition('uid', $account->uid)
        ->execute();
      break;
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
