# DatabaseConnection_sqlite::PDOPrepare()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 264–266 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L264-L266)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function PDOPrepare($query, array $options = array())
```

## Documentation

```text
NEVER CALL THIS FUNCTION: YOU MIGHT DEADLOCK YOUR PHP PROCESS.

This is a wrapper around the parent PDO::prepare method. However, as
the PDO SQLite driver only closes SELECT statements when the PDOStatement
destructor is called and SQLite does not allow data change (INSERT,
UPDATE etc) on a table which has open SELECT statements, you should never
call this function and keep a PDOStatement object alive as that can lead
to a deadlock. This really, really should be private, but as
DatabaseStatement_sqlite needs to call it, we have no other choice but to
expose this function to the world.
```

## Code

```php
  public function PDOPrepare($query, array $options = array()) {
    return $this->connection->prepare($query, $options);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
