# DatabaseConnection_sqlite::__construct()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 57–126 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L57-L126)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function __construct(array $connection_options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct(array $connection_options = array()) {
    // We don't need a specific PDOStatement class here, we simulate it below.
    $this->statementClass = NULL;

    // This driver defaults to transaction support, except if explicitly passed FALSE.
    $this->transactionSupport = $this->transactionalDDLSupport = !isset($connection_options['transactions']) || $connection_options['transactions'] !== FALSE;

    $this->connectionOptions = $connection_options;

    // Allow PDO options to be overridden.
    $connection_options += array(
      'pdo' => array(),
    );
    $connection_options['pdo'] += array(
      // Convert numeric values to strings when fetching.
      PDO::ATTR_STRINGIFY_FETCHES => TRUE,
    );
    parent::__construct('sqlite:' . $connection_options['database'], '', '', $connection_options['pdo']);

    // Attach one database for each registered prefix.
    $prefixes = $this->prefixes;
    foreach ($prefixes as $table => &$prefix) {
      // Empty prefix means query the main database -- no need to attach anything.
      if (!empty($prefix)) {
        // Only attach the database once.
        if (!isset($this->attachedDatabases[$prefix])) {
          $this->attachedDatabases[$prefix] = $prefix;
          $this->query('ATTACH DATABASE :database AS :prefix', array(':database' => $connection_options['database'] . '-' . $prefix, ':prefix' => $prefix));
        }

        // Add a ., so queries become prefix.table, which is proper syntax for
        // querying an attached database.
        $prefix .= '.';
      }
    }
    // Regenerate the prefixes replacement table.
    $this->setPrefix($prefixes);

    // Detect support for SAVEPOINT.
    $version = $this->query('SELECT sqlite_version()')->fetchField();
    $this->savepointSupport = (version_compare($version, '3.6.8') >= 0);

    // Create functions needed by SQLite.
    $this->sqliteCreateFunction('if', array($this, 'sqlFunctionIf'));
    $this->sqliteCreateFunction('greatest', array($this, 'sqlFunctionGreatest'));
    $this->sqliteCreateFunction('pow', 'pow', 2);
    $this->sqliteCreateFunction('length', 'strlen', 1);
    $this->sqliteCreateFunction('md5', 'md5', 1);
    $this->sqliteCreateFunction('concat', array($this, 'sqlFunctionConcat'));
    $this->sqliteCreateFunction('substring', array($this, 'sqlFunctionSubstring'), 3);
    $this->sqliteCreateFunction('substring_index', array($this, 'sqlFunctionSubstringIndex'), 3);
    $this->sqliteCreateFunction('rand', array($this, 'sqlFunctionRand'));

    // Enable the Write-Ahead Logging (WAL) option for SQLite if supported.
    // @see https://www.drupal.org/node/2348137
    // @see https://sqlite.org/wal.html
    if (version_compare($version, '3.7') >= 0) {
      $connection_options += array(
        'init_commands' => array(),
      );
      $connection_options['init_commands'] += array(
        'wal' => "PRAGMA journal_mode=WAL",
      );
    }

    // Execute sqlite init_commands.
    if (isset($connection_options['init_commands'])) {
      $this->connection->exec(implode('; ', $connection_options['init_commands']));
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
