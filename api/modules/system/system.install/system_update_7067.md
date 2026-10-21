# system_update_7067()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3146–3165 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3146-L3165)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7067()
```

## Documentation

```text
Grant administrators permission to view the administration theme.
```

## Code

```php
function system_update_7067() {
  // Users with access to administration pages already see the administration
  // theme in some places (if one is enabled on the site), so we want them to
  // continue seeing it.
  $admin_roles = user_roles(FALSE, 'access administration pages');
  foreach (array_keys($admin_roles) as $rid) {
    _update_7000_user_role_grant_permissions($rid, array('view the administration theme'), 'system');
  }
  // The above check is not guaranteed to reach all administrative users of the
  // site, so if the site is currently using an administration theme, display a
  // message also.
  if (variable_get('admin_theme')) {
    if (empty($admin_roles)) {
      drupal_set_message('The new "View the administration theme" permission is required in order to view your site\'s administration theme. You can grant this permission to your site\'s administrators on the <a href="' . url('admin/people/permissions', array('fragment' => 'module-system')) . '">permissions page</a>.');
    }
    else {
      drupal_set_message('The new "View the administration theme" permission is required in order to view your site\'s administration theme. This permission has been automatically granted to the following roles: <em>' . check_plain(implode(', ', $admin_roles)) . '</em>. You can grant this permission to other roles on the <a href="' . url('admin/people/permissions', array('fragment' => 'module-system')) . '">permissions page</a>.');
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
