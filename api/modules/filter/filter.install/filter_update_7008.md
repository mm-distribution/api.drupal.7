# filter_update_7008()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 447–463 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L447-L463)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7008()
```

## Documentation

```text
Grant usage of all text formats to user roles having the 'administer filters' permission.
```

## Code

```php
function filter_update_7008() {
  // Build the list of permissions to grant.
  $permissions = array();
  foreach (db_query('SELECT format FROM {filter_format}')->fetchCol() as $format_id) {
    if ($format_id != variable_get('filter_fallback_format')) {
      $permissions[] = 'use text format ' . $format_id;
    }
  }
  // Grant text format permissions to all roles that can 'administer filters'.
  // Albeit anonymous users *should not* have the permission, we cannot presume
  // that they do not or must not.
  if ($roles = user_roles(FALSE, 'administer filters')) {
    foreach ($roles as $rid => $name) {
      _update_7000_user_role_grant_permissions($rid, $permissions, 'filter');
    }
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
