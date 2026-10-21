# DatabaseConnection_sqlite::getAttachedDatabases()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 169–171 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L169-L171)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function getAttachedDatabases()
```

## Documentation

```text
Gets all the attached databases.

@return array
  An array of attached database names.

@see DatabaseConnection_sqlite::__construct().
```

## Code

```php
  public function getAttachedDatabases() {
    return $this->attachedDatabases;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
