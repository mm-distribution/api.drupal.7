# DatabaseSchema::addIndex()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 635–635 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L635)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function addIndex($table, $name, $fields);
```

## Documentation

```text
Add an index.

@param $table
  The table to be altered.
@param $name
  The name of the index.
@param $fields
  An array of field names.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table doesn't exist.
@throws DatabaseSchemaObjectExistsException
  If the specified table already has an index by that name.
```

## Code

```php
  abstract public function addIndex($table, $name, $fields);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
