# _dblog_get_message_types()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 130–139 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L130-L139)
- **Module/theme:** dblog

## Signature

```php
function _dblog_get_message_types()
```

## Documentation

```text
Gathers a list of uniquely defined database log message types.

@return array
  List of uniquely defined database log message types.
```

## Code

```php
function _dblog_get_message_types() {
  $types = array();

  $result = db_query('SELECT DISTINCT(type) FROM {watchdog} ORDER BY type');
  foreach ($result as $object) {
    $types[] = $object->type;
  }

  return $types;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
