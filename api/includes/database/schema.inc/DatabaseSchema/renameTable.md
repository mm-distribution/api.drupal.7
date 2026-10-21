# DatabaseSchema::renameTable()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 465–465 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L465)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function renameTable($table, $new_name);
```

## Documentation

```text
Rename a table.

@param $table
  The table to be renamed.
@param $new_name
  The new name for the table.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table doesn't exist.
@throws DatabaseSchemaObjectExistsException
  If a table with the specified new name already exists.
```

## Code

```php
  abstract public function renameTable($table, $new_name);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
