# user_menu()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1649–1883 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1649-L1883)
- **Module/theme:** user
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function user_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function user_menu() {
  $items['user/autocomplete'] = array(
    'title' => 'User autocomplete',
    'page callback' => 'user_autocomplete',
    'access callback' => 'user_access',
    'access arguments' => array('access user profiles'),
    'type' => MENU_CALLBACK,
    'file' => 'user.pages.inc',
  );

  // Registration and login pages.
  $items['user'] = array(
    'title' => 'User account',
    'title callback' => 'user_menu_title',
    'page callback' => 'user_page',
    'access callback' => TRUE,
    'file' => 'user.pages.inc',
    'weight' => -10,
    'menu_name' => 'user-menu',
  );

  $items['user/login'] = array(
    'title' => 'Log in',
    'access callback' => 'user_is_anonymous',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );

  $items['user/register'] = array(
    'title' => 'Create new account',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_register_form'),
    'access callback' => 'user_register_access',
    'type' => MENU_LOCAL_TASK,
  );

  $items['user/password'] = array(
    'title' => 'Request new password',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_pass'),
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'file' => 'user.pages.inc',
  );
  $items['user/reset/%/%/%'] = array(
    'title' => 'Reset password',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_pass_reset', 2, 3, 4),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
    'file' => 'user.pages.inc',
  );

  $items['user/logout'] = array(
    'title' => 'Log out',
    'access callback' => 'user_is_logged_in',
    'page callback' => 'user_logout',
    'weight' => 10,
    'menu_name' => 'user-menu',
    'file' => 'user.pages.inc',
  );

  // User listing pages.
  $items['admin/people'] = array(
    'title' => 'People',
    'description' => 'Manage user accounts, roles, and permissions.',
    'page callback' => 'user_admin',
    'page arguments' => array('list'),
    'access arguments' => array('administer users'),
    'position' => 'left',
    'weight' => -4,
    'file' => 'user.admin.inc',
  );
  $items['admin/people/people'] = array(
    'title' => 'List',
    'description' => 'Find and manage people interacting with your site.',
    'access arguments' => array('administer users'),
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
    'file' => 'user.admin.inc',
  );

  // Permissions and role forms.
  $items['admin/people/permissions'] = array(
    'title' => 'Permissions',
    'description' => 'Determine access to features by selecting permissions for roles.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_admin_permissions'),
    'access arguments' => array('administer permissions'),
    'file' => 'user.admin.inc',
    'type' => MENU_LOCAL_TASK,
  );
  $items['admin/people/permissions/list'] = array(
    'title' => 'Permissions',
    'description' => 'Determine access to features by selecting permissions for roles.',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -8,
  );
  $items['admin/people/permissions/roles'] = array(
    'title' => 'Roles',
    'description' => 'List, edit, or add user roles.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_admin_roles'),
    'access arguments' => array('administer permissions'),
    'file' => 'user.admin.inc',
    'type' => MENU_LOCAL_TASK,
    'weight' => -5,
  );
  $items['admin/people/permissions/roles/edit/%user_role'] = array(
    'title' => 'Edit role',
    'page arguments' => array('user_admin_role', 5),
    'access callback' => 'user_role_edit_access',
    'access arguments' => array(5),
  );
  $items['admin/people/permissions/roles/delete/%user_role'] = array(
    'title' => 'Delete role',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_admin_role_delete_confirm', 5),
    'access callback' => 'user_role_edit_access',
    'access arguments' => array(5),
    'file' => 'user.admin.inc',
  );

  $items['admin/people/create'] = array(
    'title' => 'Add user',
    'page callback' => 'user_admin',
    'page arguments' => array('create'),
    'access arguments' => array('administer users'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'user.admin.inc',
  );

  // Administration pages.
  $items['admin/config/people'] = array(
    'title' => 'People',
    'description' => 'Configure user accounts.',
    'position' => 'left',
    'weight' => -20,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
    'file path' => drupal_get_path('module', 'system'),
  );
  $items['admin/config/people/accounts'] = array(
    'title' => 'Account settings',
    'description' => 'Configure default behavior of users, including registration requirements, e-mails, fields, and user pictures.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_admin_settings'),
    'access arguments' => array('administer users'),
    'file' => 'user.admin.inc',
    'weight' => -10,
  );
  $items['admin/config/people/accounts/settings'] = array(
    'title' => 'Settings',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );

  $items['user/%user'] = array(
    'title' => 'My account',
    'title callback' => 'user_page_title',
    'title arguments' => array(1),
    'page callback' => 'user_view_page',
    'page arguments' => array(1),
    'access callback' => 'user_view_access',
    'access arguments' => array(1),
    // By assigning a different menu name, this item (and all registered child
    // paths) are no longer considered as children of 'user'. When accessing the
    // user account pages, the preferred menu link that is used to build the
    // active trail (breadcrumb) will be found in this menu (unless there is
    // more specific link), so the link to 'user' will not be in the breadcrumb.
    'menu_name' => 'navigation',
  );

  $items['user/%user/view'] = array(
    'title' => 'View',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );

  $items['user/%user/cancel'] = array(
    'title' => 'Cancel account',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_cancel_confirm_form', 1),
    'access callback' => 'user_cancel_access',
    'access arguments' => array(1),
    'file' => 'user.pages.inc',
  );

  $items['user/%user/cancel/confirm/%/%'] = array(
    'title' => 'Confirm account cancellation',
    'page callback' => 'user_cancel_confirm',
    'page arguments' => array(1, 4, 5),
    'access callback' => 'user_cancel_access',
    'access arguments' => array(1),
    'file' => 'user.pages.inc',
  );

  $items['user/%user/edit'] = array(
    'title' => 'Edit',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('user_profile_form', 1),
    'access callback' => 'user_edit_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'file' => 'user.pages.inc',
  );

  $items['user/%user_category/edit/account'] = array(
    'title' => 'Account',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'load arguments' => array('%map', '%index'),
  );

  if (($categories = _user_categories()) && (count($categories) > 1)) {
    foreach ($categories as $key => $category) {
      // 'account' is already handled by the MENU_DEFAULT_LOCAL_TASK.
      if ($category['name'] != 'account') {
        $items['user/%user_category/edit/' . $category['name']] = array(
          'title callback' => 'check_plain',
          'title arguments' => array($category['title']),
          'page callback' => 'drupal_get_form',
          'page arguments' => array('user_profile_form', 1, 3),
          'access callback' => isset($category['access callback']) ? $category['access callback'] : 'user_edit_access',
          'access arguments' => isset($category['access arguments']) ? $category['access arguments'] : array(1),
          'type' => MENU_LOCAL_TASK,
          'weight' => $category['weight'],
          'load arguments' => array('%map', '%index'),
          'tab_parent' => 'user/%/edit',
          'file' => 'user.pages.inc',
        );
      }
    }
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
