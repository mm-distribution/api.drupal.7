# profile_update_7001()

- **Type:** Function
- **File:** [`modules/profile/profile.install`](_file.md), lines 157–160 · [local source](../../../../source/modules/profile/profile.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install#L157-L160)
- **Module/theme:** profile

## Signature

```php
function profile_update_7001()
```

## Documentation

```text
Rename {profile_fields} table to {profile_field} and {profile_values} to {profile_value}.
```

## Code

```php
function profile_update_7001() {
  db_rename_table('profile_fields', 'profile_field');
  db_rename_table('profile_values', 'profile_value');
}
```

---
_Drupal 7.103 · [modules/profile/profile.install](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install) · Licensed GPL-2.0-or-later (see LICENSE)._
