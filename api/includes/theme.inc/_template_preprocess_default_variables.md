# _template_preprocess_default_variables()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2512–2548 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2512-L2548)

## Signature

```php
function _template_preprocess_default_variables()
```

## Documentation

```text
Returns hook-independent variables to template_preprocess().
```

## Code

```php
function _template_preprocess_default_variables() {
  global $user;

  // Variables that don't depend on a database connection.
  $variables = array(
    'attributes_array' => array(),
    'title_attributes_array' => array(),
    'content_attributes_array' => array(),
    'title_prefix' => array(),
    'title_suffix' => array(),
    'user' => $user,
    'db_is_active' => !defined('MAINTENANCE_MODE'),
    'is_admin' => FALSE,
    'logged_in' => FALSE,
  );

  // The user object has no uid property when the database does not exist during
  // install. The user_access() check deals with issues when in maintenance mode
  // as uid is set but the user.module has not been included.
  if (isset($user->uid) && function_exists('user_access')) {
    $variables['is_admin'] = user_access('access administration pages');
    $variables['logged_in'] = ($user->uid > 0);
  }

  // drupal_is_front_page() might throw an exception.
  try {
    $variables['is_front'] = drupal_is_front_page();
  }
  catch (Exception $e) {
    // If the database is not yet available, set default values for these
    // variables.
    $variables['is_front'] = FALSE;
    $variables['db_is_active'] = FALSE;
  }

  return $variables;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
