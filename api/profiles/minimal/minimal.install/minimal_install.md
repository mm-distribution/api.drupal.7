# minimal_install()

- **Type:** Function
- **File:** [`profiles/minimal/minimal.install`](_file.md), lines 14–81 · [local source](../../../../source/profiles/minimal/minimal.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/minimal/minimal.install#L14-L81)
- **Module/theme:** minimal
- **Implements:** [hook_install()](../../../modules/system/system.api.php/hook_install.md)

## Signature

```php
function minimal_install()
```

## Documentation

```text
Implements hook_install().

Performs actions to set up the site for this profile.

@see system_install()
```

## Code

```php
function minimal_install() {
  // Enable some standard blocks.
  $default_theme = variable_get('theme_default', 'bartik');
  $values = array(
    array(
      'module' => 'system',
      'delta' => 'main',
      'theme' => $default_theme,
      'status' => 1,
      'weight' => 0,
      'region' => 'content',
      'pages' => '',
      'cache' => -1,
    ),
    array(
      'module' => 'user',
      'delta' => 'login',
      'theme' => $default_theme,
      'status' => 1,
      'weight' => 0,
      'region' => 'sidebar_first',
      'pages' => '',
      'cache' => -1,
    ),
    array(
      'module' => 'system',
      'delta' => 'navigation',
      'theme' => $default_theme,
      'status' => 1,
      'weight' => 0,
      'region' => 'sidebar_first',
      'pages' => '',
      'cache' => -1,
    ),
    array(
      'module' => 'system',
      'delta' => 'management',
      'theme' => $default_theme,
      'status' => 1,
      'weight' => 1,
      'region' => 'sidebar_first',
      'pages' => '',
      'cache' => -1,
    ),
    array(
      'module' => 'system',
      'delta' => 'help',
      'theme' => $default_theme,
      'status' => 1,
      'weight' => 0,
      'region' => 'help',
      'pages' => '',
      'cache' => -1,
    ),
  );
  $query = db_insert('block')->fields(array('module', 'delta', 'theme', 'status', 'weight', 'region', 'pages', 'cache'));
  foreach ($values as $record) {
    $query->values($record);
  }
  $query->execute();

  // Allow visitor account creation, but with administrative approval.
  variable_set('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL);

  // Enable default permissions for system roles.
  user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access content'));
  user_role_grant_permissions(DRUPAL_AUTHENTICATED_RID, array('access content'));
}
```

---
_Drupal 7.103 · [profiles/minimal/minimal.install](https://github.com/drupal/drupal/blob/7.103/profiles/minimal/minimal.install) · Licensed GPL-2.0-or-later (see LICENSE)._
