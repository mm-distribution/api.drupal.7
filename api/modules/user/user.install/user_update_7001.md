# user_update_7001()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 479–483 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L479-L483)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7001()
```

## Documentation

```text
Remove the 'threshold', 'mode' and 'sort' columns from the {users} table.

These fields were previously used to store per-user comment settings.
```

## Code

```php
function user_update_7001() {
  db_drop_field('users', 'threshold');
  db_drop_field('users', 'mode');
  db_drop_field('users', 'sort');
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
