# DatabaseConnection_sqlite::sqlFunctionGreatest()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 183–196 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L183-L196)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function sqlFunctionGreatest()
```

## Documentation

```text
SQLite compatibility implementation for the GREATEST() SQL function.
```

## Code

```php
  public function sqlFunctionGreatest() {
    $args = func_get_args();
    foreach ($args as $k => $v) {
      if (!isset($v)) {
        unset($args);
      }
    }
    if (count($args)) {
      return max($args);
    }
    else {
      return NULL;
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
