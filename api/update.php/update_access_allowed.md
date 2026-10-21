# update_access_allowed()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 300–316 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L300-L316)

## Signature

```php
function update_access_allowed()
```

## Documentation

```text
Determines if the current user is allowed to run update.php.

@return
  TRUE if the current user should be granted access, or FALSE otherwise.
```

## Code

```php
function update_access_allowed() {
  global $update_free_access, $user;

  // Allow the global variable in settings.php to override the access check.
  if (!empty($update_free_access)) {
    return TRUE;
  }
  // Calls to user_access() might fail during the Drupal 6 to 7 update process,
  // so we fall back on requiring that the user be logged in as user #1.
  try {
    require_once DRUPAL_ROOT . '/' . drupal_get_path('module', 'user') . '/user.module';
    return user_access('administer software updates');
  }
  catch (Exception $e) {
    return ($user->uid == 1);
  }
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
