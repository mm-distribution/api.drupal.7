# DatabaseSchema::fieldSetDefault()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 534–534 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L534)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function fieldSetDefault($table, $field, $default);
```

## Documentation

```text
Set the default value for a field.

@param $table
  The table to be altered.
@param $field
  The field to be altered.
@param $default
  Default value to be set. NULL for 'default NULL'.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table or field doesn't exist.
```

## Code

```php
  abstract public function fieldSetDefault($table, $field, $default);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
