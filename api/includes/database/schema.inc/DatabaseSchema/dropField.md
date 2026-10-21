# DatabaseSchema::dropField()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 519–519 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L519)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
abstract public function dropField($table, $field);
```

## Documentation

```text
Drop a field.

@param $table
  The table to be altered.
@param $field
  The field to be dropped.

@return
  TRUE if the field was successfully dropped, FALSE if there was no field
  by that name to begin with.
```

## Code

```php
  abstract public function dropField($table, $field);
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
