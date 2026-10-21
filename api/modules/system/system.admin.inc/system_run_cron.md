# system_run_cron()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2374–2388 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2374-L2388)
- **Module/theme:** system

## Signature

```php
function system_run_cron()
```

## Documentation

```text
Menu callback: run cron manually.
```

## Code

```php
function system_run_cron() {
  if (!isset($_GET['token']) || !drupal_valid_token($_GET['token'], 'run-cron')) {
    return MENU_ACCESS_DENIED;
  }

  // Run cron manually
  if (drupal_cron_run()) {
    drupal_set_message(t('Cron ran successfully.'));
  }
  else {
    drupal_set_message(t('Cron run failed.'), 'error');
  }

  drupal_goto('admin/reports/status');
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
