# db_add_field()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2976–2978 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2976-L2978)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_add_field($table, $field, $spec, $keys_new = array())
```

## Documentation

```text
Adds a new field to a table.

@param $table
  Name of the table to be altered.
@param $field
  Name of the field to be added.
@param $spec
  The field specification array, as taken from a schema definition. The
  specification may also contain the key 'initial'; the newly-created field
  will be set to the value of the key in all rows. This is most useful for
  creating NOT NULL columns with no default value in existing tables.
@param $keys_new
  (optional) Keys and indexes specification to be created on the table along
  with adding the field. The format is the same as a table specification, but
  without the 'fields' element. If you are adding a type 'serial' field, you
  MUST specify at least one key or index including it in this array. See
  db_change_field() for more explanation why.

@see db_change_field()
```

## Code

```php
function db_add_field($table, $field, $spec, $keys_new = array()) {
  return Database::getConnection()->schema()->addField($table, $field, $spec, $keys_new);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
