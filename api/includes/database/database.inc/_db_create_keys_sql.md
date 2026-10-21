# _db_create_keys_sql()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2929–2931 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2929-L2931)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function _db_create_keys_sql($spec)
```

## Documentation

_No docblock in source._

## Code

```php
function _db_create_keys_sql($spec) {
  return Database::getConnection()->schema()->createKeysSql($spec);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
