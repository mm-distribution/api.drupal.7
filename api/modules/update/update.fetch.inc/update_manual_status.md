# update_manual_status()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 15–29 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L15-L29)
- **Module/theme:** update

## Signature

```php
function update_manual_status()
```

## Documentation

```text
Page callback: Checks for updates and displays the update status report.

Manually checks the update status without the use of cron.

@see update_menu()
```

## Code

```php
function update_manual_status() {
  _update_refresh();
  $batch = array(
    'operations' => array(
      array('update_fetch_data_batch', array()),
    ),
    'finished' => 'update_fetch_data_finished',
    'title' => t('Checking available update data'),
    'progress_message' => t('Trying to check available update data ...'),
    'error_message' => t('Error checking available update data.'),
    'file' => drupal_get_path('module', 'update') . '/update.fetch.inc',
  );
  batch_set($batch);
  batch_process('admin/reports/updates');
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
