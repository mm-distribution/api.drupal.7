# db_drop_field()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2988–2990 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2988-L2990)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_drop_field($table, $field)
```

## Documentation

```text
Drops a field.

@param $table
  The table to be altered.
@param $field
  The field to be dropped.
```

## Code

```php
function db_drop_field($table, $field) {
  return Database::getConnection()->schema()->dropField($table, $field);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
