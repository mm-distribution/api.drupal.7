# statistics_user_cancel()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 222–231 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L222-L231)
- **Module/theme:** statistics
- **Implements:** [hook_user_cancel()](../../user/user.api.php/hook_user_cancel.md)

## Signature

```php
function statistics_user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements hook_user_cancel().
```

## Code

```php
function statistics_user_cancel($edit, $account, $method) {
  switch ($method) {
    case 'user_cancel_reassign':
      db_update('accesslog')
        ->fields(array('uid' => 0))
        ->condition('uid', $account->uid)
        ->execute();
      break;
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
