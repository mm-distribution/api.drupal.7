# system_status()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2348–2369 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2348-L2369)
- **Module/theme:** system

## Signature

```php
function system_status($check = FALSE)
```

## Documentation

```text
Menu callback: displays the site status report. Can also be used as a pure check.

@param $check
  If true, only returns a boolean whether there are system status errors.
```

## Code

```php
function system_status($check = FALSE) {
  // Load .install files
  include_once DRUPAL_ROOT . '/includes/install.inc';
  drupal_load_updates();

  // Check run-time requirements and status information.
  $requirements = module_invoke_all('requirements', 'runtime');
  usort($requirements, '_system_sort_requirements');

  if ($check) {
    return drupal_requirements_severity($requirements) == REQUIREMENT_ERROR;
  }
  // MySQL import might have set the uid of the anonymous user to autoincrement
  // value. Let's try fixing it. See http://drupal.org/node/204411
  db_update('users')
    ->expression('uid', 'uid - uid')
    ->condition('name', '')
    ->condition('pass', '')
    ->condition('status', 0)
    ->execute();
  return theme('status_report', array('requirements' => $requirements));
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
