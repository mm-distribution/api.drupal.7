# dblog_update_7003()

- **Type:** Function
- **File:** [`modules/dblog/dblog.install`](_file.md), lines 160–164 · [local source](../../../../source/modules/dblog/dblog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install#L160-L164)
- **Module/theme:** dblog
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function dblog_update_7003()
```

## Documentation

```text
Account for possible legacy systems where dblog was not installed.
```

## Code

```php
function dblog_update_7003() {
  if (!db_table_exists('watchdog')) {
    db_create_table('watchdog', drupal_get_schema_unprocessed('dblog', 'watchdog'));
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.install](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
