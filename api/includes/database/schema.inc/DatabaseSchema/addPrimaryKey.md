# DatabaseSchema::addPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 575–575 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L575)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function addPrimaryKey($table, $fields);
```

## Documentation

```text
Add a primary key.

@param $table
  The table to be altered.
@param $fields
  Fields for the primary key.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table doesn't exist.
@throws DatabaseSchemaObjectExistsException
  If the specified table already has a primary key.
```

## Code

```php
  abstract public function addPrimaryKey($table, $fields);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
