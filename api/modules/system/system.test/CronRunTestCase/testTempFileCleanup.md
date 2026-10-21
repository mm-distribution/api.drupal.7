# CronRunTestCase::testTempFileCleanup()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 875–913 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L875-L913)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
function testTempFileCleanup()
```

## Documentation

```text
Ensure that temporary files are removed.

Create files for all the possible combinations of age and status. We are
using UPDATE statements rather than file_save() because it would set the
timestamp.
```

## Code

```php
  function testTempFileCleanup() {
    // Temporary file that is older than DRUPAL_MAXIMUM_TEMP_FILE_AGE.
    $temp_old = file_save_data('');
    db_update('file_managed')
      ->fields(array(
        'status' => 0,
        'timestamp' => 1,
      ))
      ->condition('fid', $temp_old->fid)
      ->execute();
    $this->assertTrue(file_exists($temp_old->uri), 'Old temp file was created correctly.');

    // Temporary file that is less than DRUPAL_MAXIMUM_TEMP_FILE_AGE.
    $temp_new = file_save_data('');
    db_update('file_managed')
      ->fields(array('status' => 0))
      ->condition('fid', $temp_new->fid)
      ->execute();
    $this->assertTrue(file_exists($temp_new->uri), 'New temp file was created correctly.');

    // Permanent file that is older than DRUPAL_MAXIMUM_TEMP_FILE_AGE.
    $perm_old = file_save_data('');
    db_update('file_managed')
      ->fields(array('timestamp' => 1))
      ->condition('fid', $temp_old->fid)
      ->execute();
    $this->assertTrue(file_exists($perm_old->uri), 'Old permanent file was created correctly.');

    // Permanent file that is newer than DRUPAL_MAXIMUM_TEMP_FILE_AGE.
    $perm_new = file_save_data('');
    $this->assertTrue(file_exists($perm_new->uri), 'New permanent file was created correctly.');

    // Run cron and then ensure that only the old, temp file was deleted.
    $this->cronRun();
    $this->assertFalse(file_exists($temp_old->uri), 'Old temp file was correctly removed.');
    $this->assertTrue(file_exists($temp_new->uri), 'New temp file was correctly ignored.');
    $this->assertTrue(file_exists($perm_old->uri), 'Old permanent file was correctly ignored.');
    $this->assertTrue(file_exists($perm_new->uri), 'New permanent file was correctly ignored.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
