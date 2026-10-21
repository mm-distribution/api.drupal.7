# DatabaseConnection_sqlite::prepare()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 248–250 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L248-L250)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function prepare($query, $options = array())
```

## Documentation

```text
SQLite-specific implementation of DatabaseConnection::prepare().

We don't use prepared statements at all at this stage. We just create
a DatabaseStatement_sqlite object, that will create a PDOStatement
using the semi-private PDOPrepare() method below.
```

## Code

```php
  public function prepare($query, $options = array()) {
    return new DatabaseStatement_sqlite($this, $query, $options);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
