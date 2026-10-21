# DatabaseSchema::dropIndex()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 649–649 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L649)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function dropIndex($table, $name);
```

## Documentation

```text
Drop an index.

@param $table
  The table to be altered.
@param $name
  The name of the index.

@return
  TRUE if the index was successfully dropped, FALSE if there was no index
  by that name to begin with.
```

## Code

```php
  abstract public function dropIndex($table, $name);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
