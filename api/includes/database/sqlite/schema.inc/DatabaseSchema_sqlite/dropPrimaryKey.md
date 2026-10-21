# DatabaseSchema_sqlite::dropPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 634–645 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L634-L645)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function dropPrimaryKey($table)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropPrimaryKey($table) {
    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    if (empty($new_schema['primary key'])) {
      return FALSE;
    }

    unset($new_schema['primary key']);
    $this->alterTable($table, $old_schema, $new_schema);
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
