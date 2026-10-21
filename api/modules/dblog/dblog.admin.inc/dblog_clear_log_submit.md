# dblog_clear_log_submit()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 427–431 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L427-L431)
- **Module/theme:** dblog

## Signature

```php
function dblog_clear_log_submit()
```

## Documentation

```text
Form submission handler for dblog_clear_log_form().
```

## Code

```php
function dblog_clear_log_submit() {
  $_SESSION['dblog_overview_filter'] = array();
  db_truncate('watchdog')->execute();
  drupal_set_message(t('Database log cleared.'));
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
