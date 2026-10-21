# dashboard_uninstall()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.install`](_file.md), lines 76–78 · [local source](../../../../source/modules/dashboard/dashboard.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install#L76-L78)
- **Module/theme:** dashboard
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function dashboard_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function dashboard_uninstall() {
  variable_del('dashboard_stashed_blocks');
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.install](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.install) · Licensed GPL-2.0-or-later (see LICENSE)._
