# db_like()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2730–2732 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2730-L2732)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_like($string)
```

## Documentation

```text
Escapes characters that work as wildcard characters in a LIKE pattern.

The wildcard characters "%" and "_" as well as backslash are prefixed with
a backslash. Use this to do a search for a verbatim string without any
wildcard behavior.

For example, the following does a case-insensitive query for all rows whose
name starts with $prefix:
@code
$result = db_query(
  'SELECT * FROM person WHERE name LIKE :pattern',
  array(':pattern' => db_like($prefix) . '%')
);
@endcode

Backslash is defined as escape character for LIKE patterns in
DatabaseCondition::mapConditionOperator().

@param $string
  The string to escape.

@return
  The escaped string.
```

## Code

```php
function db_like($string) {
  return Database::getConnection()->escapeLike($string);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
