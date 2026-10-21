# db_field_names()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2852–2854 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2852-L2854)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_field_names($fields)
```

## Documentation

```text
Returns an array of field names from an array of key/index column specifiers.

This is usually an identity function but if a key/index uses a column prefix
specification, this function extracts just the name.

@param $fields
  An array of key/index column specifiers.

@return
  An array of field names.
```

## Code

```php
function db_field_names($fields) {
  return Database::getConnection()->schema()->fieldNames($fields);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
