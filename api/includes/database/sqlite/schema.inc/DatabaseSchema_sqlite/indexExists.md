# DatabaseSchema_sqlite::indexExists()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 575–579 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L575-L579)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function indexExists($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function indexExists($table, $name) {
    $info = $this->getPrefixInfo($table);

    return $this->connection->query('PRAGMA ' . $info['schema'] . '.index_info(' . $info['table'] . '_' . $name . ')')->fetchField() != '';
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
