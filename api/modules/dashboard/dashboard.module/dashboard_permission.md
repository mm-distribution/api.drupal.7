# dashboard_permission()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 84–96 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L84-L96)
- **Module/theme:** dashboard
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function dashboard_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function dashboard_permission() {
  return array(
    'access dashboard' => array(
      'title' => t('View the administrative dashboard'),
      // Note: We translate the 'Administer blocks' permission string here with
      // a separate t() call, to make sure it gets the same translation as when
      // it's in block_permission().
      'description' => t('Customizing the dashboard requires the !permission-name permission.', array(
        '!permission-name' => l(t('Administer blocks'), 'admin/people/permissions', array('fragment' => 'module-block')),
      )),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
