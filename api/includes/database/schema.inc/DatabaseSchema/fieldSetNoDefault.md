# DatabaseSchema::fieldSetNoDefault()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 547–547 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L547)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function fieldSetNoDefault($table, $field);
```

## Documentation

```text
Set a field to have no default value.

@param $table
  The table to be altered.
@param $field
  The field to be altered.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table or field doesn't exist.
```

## Code

```php
  abstract public function fieldSetNoDefault($table, $field);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
