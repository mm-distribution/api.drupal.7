# DatabaseConnection_sqlite::__destruct()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 135–159 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L135-L159)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function __destruct()
```

## Documentation

```text
Destructor for the SQLite connection.

We prune empty databases on destruct, but only if tables have been
dropped. This is especially needed when running the test suite, which
creates and destroy databases several times in a row.
```

## Code

```php
  public function __destruct() {
    if ($this->tableDropped && !empty($this->attachedDatabases)) {
      if (!is_array($this->attachedDatabases)) {
        throw new UnexpectedValueException();
      }
      foreach ($this->attachedDatabases as $prefix) {
        // Check if the database is now empty, ignore the internal SQLite tables.
        try {
          $count = $this->query('SELECT COUNT(*) FROM ' . $prefix . '.sqlite_master WHERE type = :type AND name NOT LIKE :pattern', array(':type' => 'table', ':pattern' => 'sqlite_%'))->fetchField();

          // We can prune the database file if it doesn't have any tables.
          if ($count == 0 && $this->connectionOptions['database'] != ':memory:') {
            // Detaching the database fails at this point, but no other queries
            // are executed after the connection is destructed so we can simply
            // remove the database file.
            unlink($this->connectionOptions['database'] . '-' . $prefix);
          }
        }
        catch (Exception $e) {
          // Ignore the exception and continue. There is nothing we can do here
          // to report the error or fail safe.
        }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
