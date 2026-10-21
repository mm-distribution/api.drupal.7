# update_init()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 111–160 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L111-L160)
- **Module/theme:** update
- **Implements:** [hook_init()](../../system/system.api.php/hook_init.md)

## Signature

```php
function update_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function update_init() {
  if (arg(0) == 'admin' && user_access('administer site configuration')) {
    switch ($_GET['q']) {
      // These pages don't need additional nagging.
      case 'admin/appearance/update':
      case 'admin/appearance/install':
      case 'admin/modules/update':
      case 'admin/modules/install':
      case 'admin/reports/updates':
      case 'admin/reports/updates/update':
      case 'admin/reports/updates/install':
      case 'admin/reports/updates/settings':
      case 'admin/reports/status':
      case 'admin/update/ready':
        return;

      // If we are on the appearance or modules list, display a detailed report
      // of the update status.
      case 'admin/appearance':
      case 'admin/modules':
        $verbose = TRUE;
        break;

    }
    module_load_install('update');
    $status = update_requirements('runtime');
    foreach (array('core', 'contrib') as $report_type) {
      $type = 'update_' . $report_type;
      if (!empty($verbose)) {
        if (isset($status[$type]['severity'])) {
          if ($status[$type]['severity'] == REQUIREMENT_ERROR) {
            drupal_set_message($status[$type]['description'], 'error', FALSE);
          }
          elseif ($status[$type]['severity'] == REQUIREMENT_WARNING) {
            drupal_set_message($status[$type]['description'], 'warning', FALSE);
          }
        }
      }
      // Otherwise, if we're on *any* admin page and there's a security
      // update missing, print an error message about it.
      else {
        if (isset($status[$type])
            && isset($status[$type]['reason'])
            && $status[$type]['reason'] === UPDATE_NOT_SECURE) {
          drupal_set_message($status[$type]['description'], 'error', FALSE);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
