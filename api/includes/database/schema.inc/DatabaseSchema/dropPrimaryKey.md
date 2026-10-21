# DatabaseSchema::dropPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 587–587 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L587)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function dropPrimaryKey($table);
```

## Documentation

```text
Drop the primary key.

@param $table
  The table to be altered.

@return
  TRUE if the primary key was successfully dropped, FALSE if there was no
  primary key on this table to begin with.
```

## Code

```php
  abstract public function dropPrimaryKey($table);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
