# db_drop_index()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3088–3090 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3088-L3090)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_drop_index($table, $name)
```

## Documentation

```text
Drops an index.

@param $table
  The table to be altered.
@param $name
  The name of the index.
```

## Code

```php
function db_drop_index($table, $name) {
  return Database::getConnection()->schema()->dropIndex($table, $name);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
