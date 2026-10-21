# DatabaseSchema::dropUniqueKey()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 618–618 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L618)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function dropUniqueKey($table, $name);
```

## Documentation

```text
Drop a unique key.

@param $table
  The table to be altered.
@param $name
  The name of the key.

@return
  TRUE if the key was successfully dropped, FALSE if there was no key by
  that name to begin with.
```

## Code

```php
  abstract public function dropUniqueKey($table, $name);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
