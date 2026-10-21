# DatabaseSchema::prefixNonTable()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 267–272 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L267-L272)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
function prefixNonTable($table)
```

## Documentation

```text
Create names for indexes, primary keys and constraints.

This prevents using {} around non-table names like indexes and keys.
```

## Code

```php
  function prefixNonTable($table) {
    $args = func_get_args();
    $info = $this->getPrefixInfo($table);
    $args[0] = $info['table'];
    return implode('_', $args);
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
