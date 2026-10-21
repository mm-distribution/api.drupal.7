# authorize_access_allowed()

- **Type:** Function
- **File:** [`authorize.php`](_file.md), lines 57–59 · [local source](../../source/authorize.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/authorize.php#L57-L59)

## Signature

```php
function authorize_access_allowed()
```

## Documentation

```text
Determines if the current user is allowed to run authorize.php.

The killswitch in settings.php overrides all else, otherwise, the user must
have access to the 'administer software updates' permission.

@return
  TRUE if the current user can run authorize.php, and FALSE if not.
```

## Code

```php
function authorize_access_allowed() {
  return variable_get('allow_authorize_operations', TRUE) && user_access('administer software updates');
}
```

---
_Drupal 7.103 · [authorize.php](https://github.com/drupal/drupal/blob/7.103/authorize.php) · Licensed GPL-2.0-or-later (see LICENSE)._
