# user_theme()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 108–148 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L108-L148)
- **Module/theme:** user
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function user_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function user_theme() {
  return array(
    'user_picture' => array(
      'variables' => array('account' => NULL),
      'template' => 'user-picture',
    ),
    'user_profile' => array(
      'render element' => 'elements',
      'template' => 'user-profile',
      'file' => 'user.pages.inc',
    ),
    'user_profile_category' => array(
      'render element' => 'element',
      'template' => 'user-profile-category',
      'file' => 'user.pages.inc',
    ),
    'user_profile_item' => array(
      'render element' => 'element',
      'template' => 'user-profile-item',
      'file' => 'user.pages.inc',
    ),
    'user_list' => array(
      'variables' => array('users' => NULL, 'title' => NULL),
    ),
    'user_admin_permissions' => array(
      'render element' => 'form',
      'file' => 'user.admin.inc',
    ),
    'user_admin_roles' => array(
      'render element' => 'form',
      'file' => 'user.admin.inc',
    ),
    'user_permission_description' => array(
      'variables' => array('permission_item' => NULL, 'hide' => NULL),
      'file' => 'user.admin.inc',
    ),
    'user_signature' => array(
      'variables' => array('signature' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
