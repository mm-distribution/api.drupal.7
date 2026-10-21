# dblog_update_7002()

- **Type:** Function
- **File:** [`modules/dblog/dblog.install`](_file.md), lines 153–155 · [local source](../../../../source/modules/dblog/dblog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install#L153-L155)
- **Module/theme:** dblog
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function dblog_update_7002()
```

## Documentation

```text
Add an index to the severity column in the watchdog database table.
```

## Code

```php
function dblog_update_7002() {
  db_add_index('watchdog', 'severity', array('severity'));
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.install](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
