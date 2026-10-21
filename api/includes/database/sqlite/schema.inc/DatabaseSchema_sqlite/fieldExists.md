# DatabaseSchema_sqlite::fieldExists()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 28–31 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L28-L31)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function fieldExists($table, $column)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fieldExists($table, $column) {
    $schema = $this->introspectSchema($table);
    return !empty($schema['fields'][$column]);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
