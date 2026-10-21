# dblog_cron()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 101–122 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L101-L122)
- **Module/theme:** dblog
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function dblog_cron()
```

## Documentation

```text
Implements hook_cron().

Controls the size of the log table, paring it to 'dblog_row_limit' messages.
```

## Code

```php
function dblog_cron() {
  // Cleanup the watchdog table.
  $row_limit = variable_get('dblog_row_limit', 1000);

  // For row limit n, get the wid of the nth row in descending wid order.
  // Counting the most recent n rows avoids issues with wid number sequences,
  // e.g. auto_increment value > 1 or rows deleted directly from the table.
  if ($row_limit > 0) {
    $min_row = db_select('watchdog', 'w')
      ->fields('w', array('wid'))
      ->orderBy('wid', 'DESC')
      ->range($row_limit - 1, 1)
      ->execute()->fetchField();

    // Delete all table entries older than the nth row, if nth row was found.
    if ($min_row) {
      db_delete('watchdog')
        ->condition('wid', $min_row, '<')
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
