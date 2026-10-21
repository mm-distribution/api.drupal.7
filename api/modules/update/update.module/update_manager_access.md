# update_manager_access()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 263–265 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L263-L265)
- **Module/theme:** update

## Signature

```php
function update_manager_access()
```

## Documentation

```text
Access callback: Resolves if the current user can access updater menu items.

It both enforces the 'administer software updates' permission and the global
kill switch for the authorize.php script.

@return
  TRUE if the current user can access the updater menu items; FALSE
  otherwise.

@see update_menu()
```

## Code

```php
function update_manager_access() {
  return variable_get('allow_authorize_operations', TRUE) && user_access('administer software updates');
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
