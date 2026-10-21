# db_drop_unique_key()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3062–3064 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3062-L3064)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_drop_unique_key($table, $name)
```

## Documentation

```text
Drops a unique key.

@param $table
  The table to be altered.
@param $name
  The name of the key.
```

## Code

```php
function db_drop_unique_key($table, $name) {
  return Database::getConnection()->schema()->dropUniqueKey($table, $name);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
