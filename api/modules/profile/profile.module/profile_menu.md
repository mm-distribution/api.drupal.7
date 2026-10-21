# profile_menu()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 79–134 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L79-L134)
- **Module/theme:** profile
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function profile_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function profile_menu() {
  $items['profile'] = array(
    'title' => 'User list',
    'page callback' => 'profile_browse',
    'access arguments' => array('access user profiles'),
    'file' => 'profile.pages.inc',
    'type' => MENU_SUGGESTED_ITEM,
  );
  $items['admin/config/people/profile'] = array(
    'title' => 'Profiles',
    'description' => 'Create customizable fields for your users.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('profile_admin_overview'),
    'access arguments' => array('administer users'),
    'file' => 'profile.admin.inc',
  );
  $items['admin/config/people/profile/add'] = array(
    'title' => 'Add field',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('profile_field_form'),
    'access arguments' => array('administer users'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'profile.admin.inc',
  );
  $items['admin/config/people/profile/autocomplete'] = array(
    'title' => 'Profile category autocomplete',
    'page callback' => 'profile_admin_settings_autocomplete',
    'access arguments' => array('administer users'),
    'file' => 'profile.admin.inc',
    'type' => MENU_CALLBACK,
  );
  $items['admin/config/people/profile/edit'] = array(
    'title' => 'Edit field',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('profile_field_form'),
    'access arguments' => array('administer users'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'profile.admin.inc',
  );
  $items['admin/config/people/profile/delete'] = array(
    'title' => 'Delete field',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('profile_field_delete'),
    'access arguments' => array('administer users'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'profile.admin.inc',
  );
  $items['profile/autocomplete'] = array(
    'title' => 'Profile autocomplete',
    'page callback' => 'profile_autocomplete',
    'access arguments' => array('access user profiles'),
    'file' => 'profile.pages.inc',
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
