# filter_access()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1031–1045 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1031-L1045)
- **Module/theme:** filter

## Signature

```php
function filter_access($format, $account = NULL)
```

## Documentation

```text
Checks if a user has access to a particular text format.

@param $format
  An object representing the text format.
@param $account
  (optional) The user account to check access for; if omitted, the currently
  logged-in user is used. Defaults to NULL.

@return
  Boolean TRUE if the user is allowed to access the given format.
```

## Code

```php
function filter_access($format, $account = NULL) {
  global $user;
  if (!isset($account)) {
    $account = $user;
  }
  // Handle special cases up front. All users have access to the fallback
  // format.
  if ($format->format == filter_fallback_format()) {
    return TRUE;
  }
  // Check the permission if one exists; otherwise, we have a non-existent
  // format so we return FALSE.
  $permission = filter_permission_name($format);
  return !empty($permission) && user_access($permission, $account);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
