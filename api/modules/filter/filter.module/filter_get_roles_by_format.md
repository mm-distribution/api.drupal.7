# filter_get_roles_by_format()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 475–483 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L475-L483)
- **Module/theme:** filter

## Signature

```php
function filter_get_roles_by_format($format)
```

## Documentation

```text
Retrieves a list of roles that are allowed to use a given text format.

@param $format
  An object representing the text format.

@return
  An array of role names, keyed by role ID.
```

## Code

```php
function filter_get_roles_by_format($format) {
  // Handle the fallback format upfront (all roles have access to this format).
  if ($format->format == filter_fallback_format()) {
    return user_roles();
  }
  // Do not list any roles if the permission does not exist.
  $permission = filter_permission_name($format);
  return !empty($permission) ? user_roles(FALSE, $permission) : array();
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
