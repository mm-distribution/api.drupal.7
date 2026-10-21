# statistics_user_delete()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 236–240 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L236-L240)
- **Module/theme:** statistics
- **Implements:** [hook_user_delete()](../../user/user.api.php/hook_user_delete.md)

## Signature

```php
function statistics_user_delete($account)
```

## Documentation

```text
Implements hook_user_delete().
```

## Code

```php
function statistics_user_delete($account) {
  db_delete('accesslog')
    ->condition('uid', $account->uid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
