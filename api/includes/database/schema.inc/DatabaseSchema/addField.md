# DatabaseSchema::addField()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 505–505 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L505)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function addField($table, $field, $spec, $keys_new = array());
```

## Documentation

```text
Add a new field to a table.

@param $table
  Name of the table to be altered.
@param $field
  Name of the field to be added.
@param $spec
  The field specification array, as taken from a schema definition.
  The specification may also contain the key 'initial', the newly
  created field will be set to the value of the key in all rows.
  This is most useful for creating NOT NULL columns with no default
  value in existing tables.
@param $keys_new
  (optional) Keys and indexes specification to be created on the
  table along with adding the field. The format is the same as a
  table specification but without the 'fields' element. If you are
  adding a type 'serial' field, you MUST specify at least one key
  or index including it in this array. See db_change_field() for more
  explanation why.

@throws DatabaseSchemaObjectDoesNotExistException
  If the specified table doesn't exist.
@throws DatabaseSchemaObjectExistsException
  If the specified table already has a field by that name.
```

## Code

```php
  abstract public function addField($table, $field, $spec, $keys_new = array());
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
