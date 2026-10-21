# user_update_7014()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 825–832 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L825-L832)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7014()
```

## Documentation

```text
Rename the 'post comments without approval' permission.

In Drupal 7, this permission has been renamed to 'skip comment approval'.
```

## Code

```php
function user_update_7014() {
  db_update('role_permission')
        ->fields(array('permission' => 'skip comment approval'))
        ->condition('permission', 'post comments without approval')
        ->execute();

  return t("Renamed the 'post comments without approval' permission to 'skip comment approval'.");
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
