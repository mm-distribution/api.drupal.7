# user_permission()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 881–906 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L881-L906)
- **Module/theme:** user
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function user_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function user_permission() {
  return array(
    'administer permissions' =>  array(
      'title' => t('Administer permissions'),
      'restrict access' => TRUE,
    ),
    'administer users' => array(
      'title' => t('Administer users'),
      'restrict access' => TRUE,
    ),
    'access user profiles' => array(
      'title' => t('View user profiles'),
    ),
    'change own username' => array(
      'title' => t('Change own username'),
    ),
    'cancel account' => array(
      'title' => t('Cancel own user account'),
      'description' => t('Note: content may be kept, unpublished, deleted or transferred to the %anonymous-name user depending on the configured <a href="@user-settings-url">user settings</a>.', array('%anonymous-name' => variable_get('anonymous', t('Anonymous')), '@user-settings-url' => url('admin/config/people/accounts'))),
    ),
    'select account cancellation method' => array(
      'title' => t('Select method for cancelling own account'),
      'restrict access' => TRUE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
