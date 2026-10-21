# _update_no_data()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 368–375 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L368-L375)
- **Module/theme:** update

## Signature

```php
function _update_no_data()
```

## Documentation

```text
Returns a warning message when there is no data about available updates.
```

## Code

```php
function _update_no_data() {
  $destination = drupal_get_destination();
  $cron_token = array('token' => drupal_get_token('run-cron'));
  return t('No update information available. <a href="@run_cron">Run cron</a> or <a href="@check_manually">check manually</a>.', array(
    '@run_cron' => url('admin/reports/status/run-cron', array('query' => $cron_token + $destination)),
    '@check_manually' => url('admin/reports/updates/check', array('query' => $destination)),
  ));
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
