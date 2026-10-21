# profile_theme()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 55–74 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L55-L74)
- **Module/theme:** profile
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function profile_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function profile_theme() {
  return array(
    'profile_block' => array(
      'variables' => array('account' => NULL, 'fields' => array()),
      'template' => 'profile-block',
    ),
    'profile_listing' => array(
      'variables' => array('account' => NULL, 'fields' => array()),
      'template' => 'profile-listing',
    ),
    'profile_wrapper' => array(
      'variables' => array('content' => NULL),
      'template' => 'profile-wrapper',
    ),
    'profile_admin_overview' => array(
      'render element' => 'form',
      'file' => 'profile.admin.inc',
    )
  );
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
