# DatabaseConnection::generateTemporaryTableName()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1259–1261 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1259-L1261)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function generateTemporaryTableName()
```

## Documentation

```text
Generates a temporary table name.

@return
  A table name.
```

## Code

```php
  protected function generateTemporaryTableName() {
    return "db_temporary_" . $this->temporaryNameIndex++;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
