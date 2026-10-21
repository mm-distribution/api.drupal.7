# DatabaseConnection::getUnprefixedTablesMap()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 523–525 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L523-L525)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getUnprefixedTablesMap()
```

## Documentation

```text
Gets a list of individually prefixed table names.

@return array
  An array of un-prefixed table names, keyed by their fully qualified table
  names (i.e. prefix + table_name).
```

## Code

```php
  public function getUnprefixedTablesMap() {
    return $this->unprefixedTablesMap;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
