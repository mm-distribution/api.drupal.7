# db_field_set_no_default()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3014–3016 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3014-L3016)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_field_set_no_default($table, $field)
```

## Documentation

```text
Sets a field to have no default value.

@param $table
  The table to be altered.
@param $field
  The field to be altered.
```

## Code

```php
function db_field_set_no_default($table, $field) {
  return Database::getConnection()->schema()->fieldSetNoDefault($table, $field);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
