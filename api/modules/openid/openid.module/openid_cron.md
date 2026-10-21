# openid_cron()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 1036–1040 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L1036-L1040)
- **Module/theme:** openid
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function openid_cron()
```

## Documentation

```text
Remove expired nonces from the database.

Implements hook_cron().
```

## Code

```php
function openid_cron() {
  db_delete('openid_nonce')
    ->condition('expires', REQUEST_TIME, '<')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
