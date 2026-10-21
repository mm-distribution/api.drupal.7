# DatabaseConnection::makeSequenceName()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 632–634 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L632-L634)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function makeSequenceName($table, $field)
```

## Documentation

```text
Creates the appropriate sequence name for a given table and serial field.

This information is exposed to all database drivers, although it is only
useful on some of them. This method is table prefix-aware.

@param $table
  The table name to use for the sequence.
@param $field
  The field name to use for the sequence.

@return
  A table prefix-parsed string for the sequence name.
```

## Code

```php
  public function makeSequenceName($table, $field) {
    return $this->prefixTables('{' . $table . '}_' . $field . '_seq');
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
