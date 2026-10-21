# db_escape_field()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2701–2703 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2701-L2703)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_escape_field($field)
```

## Documentation

```text
Restricts a dynamic column or constraint name to safe characters.

Only keeps alphanumeric and underscores.

@param $field
  The field name to escape.

@return
  The escaped field name as a string.
```

## Code

```php
function db_escape_field($field) {
  return Database::getConnection()->escapeField($field);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
