# DatabaseSchema_sqlite::mapKeyDefinition()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 547–558 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L547-L558)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function mapKeyDefinition(array $key_definition, array $mapping)
```

## Documentation

```text
Utility method: rename columns in an index definition according to a new mapping.

@param $key_definition
  The key definition.
@param $mapping
  The new mapping.
```

## Code

```php
  protected function mapKeyDefinition(array $key_definition, array $mapping) {
    foreach ($key_definition as &$field) {
      // The key definition can be an array($field, $length).
      if (is_array($field)) {
        $field = &$field[0];
      }
      if (isset($mapping[$field])) {
        $field = $mapping[$field];
      }
    }
    return $key_definition;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
