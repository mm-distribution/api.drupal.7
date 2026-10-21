# db_index_exists()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2867–2869 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2867-L2869)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_index_exists($table, $name)
```

## Documentation

```text
Checks if an index exists in the given table.

@param $table
  The name of the table in drupal (no prefixing).
@param $name
  The name of the index in drupal (no prefixing).

@return
  TRUE if the given index exists, otherwise FALSE.
```

## Code

```php
function db_index_exists($table, $name) {
  return Database::getConnection()->schema()->indexExists($table, $name);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
