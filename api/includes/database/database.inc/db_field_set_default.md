# db_field_set_default()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3002–3004 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3002-L3004)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_field_set_default($table, $field, $default)
```

## Documentation

```text
Sets the default value for a field.

@param $table
  The table to be altered.
@param $field
  The field to be altered.
@param $default
  Default value to be set. NULL for 'default NULL'.
```

## Code

```php
function db_field_set_default($table, $field, $default) {
  return Database::getConnection()->schema()->fieldSetDefault($table, $field, $default);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
