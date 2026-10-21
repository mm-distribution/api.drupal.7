# DatabaseSchema::dropTable()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 477–477 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L477)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function dropTable($table);
```

## Documentation

```text
Drop a table.

@param $table
  The table to be dropped.

@return
  TRUE if the table was successfully dropped, FALSE if there was no table
  by that name to begin with.
```

## Code

```php
  abstract public function dropTable($table);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
