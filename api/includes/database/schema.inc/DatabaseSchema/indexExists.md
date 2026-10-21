# DatabaseSchema::indexExists()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 560–560 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L560)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function indexExists($table, $name);
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
  abstract public function indexExists($table, $name);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
