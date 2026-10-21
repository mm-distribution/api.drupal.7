# DatabaseConnection_pgsql::__construct()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 20–75 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L20-L75)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
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
    // This driver defaults to transaction support, except if explicitly passed FALSE.
    $this->transactionSupport = !isset($connection_options['transactions']) || ($connection_options['transactions'] !== FALSE);

    // Transactional DDL is always available in PostgreSQL,
    // but we'll only enable it if standard transactions are.
    $this->transactionalDDLSupport = $this->transactionSupport;

    // Default to TCP connection on port 5432.
    if (empty($connection_options['port'])) {
      $connection_options['port'] = 5432;
    }

    // PostgreSQL in trust mode doesn't require a password to be supplied.
    if (empty($connection_options['password'])) {
      $connection_options['password'] = NULL;
    }
    // If the password contains a backslash it is treated as an escape character
    // http://bugs.php.net/bug.php?id=53217
    // so backslashes in the password need to be doubled up.
    // The bug was reported against pdo_pgsql 1.0.2, backslashes in passwords
    // will break on this doubling up when the bug is fixed, so check the version
    //elseif (phpversion('pdo_pgsql') < 'version_this_was_fixed_in') {
    else {
      $connection_options['password'] = str_replace('\\', '\\\\', $connection_options['password']);
    }

    $this->connectionOptions = $connection_options;

    $dsn = 'pgsql:host=' . $connection_options['host'] . ' dbname=' . $connection_options['database'] . ' port=' . $connection_options['port'];

    // Allow PDO options to be overridden.
    $connection_options += array(
      'pdo' => array(),
    );
    $connection_options['pdo'] += array(
      // Prepared statements are most effective for performance when queries
      // are recycled (used several times). However, if they are not re-used,
      // prepared statements become inefficient. Since most of Drupal's
      // prepared queries are not re-used, it should be faster to emulate
      // the preparation than to actually ready statements for re-use. If in
      // doubt, reset to FALSE and measure performance.
      PDO::ATTR_EMULATE_PREPARES => TRUE,
      // Convert numeric values to strings when fetching.
      PDO::ATTR_STRINGIFY_FETCHES => TRUE,
    );
    parent::__construct($dsn, $connection_options['username'], $connection_options['password'], $connection_options['pdo']);

    // Force PostgreSQL to use the UTF-8 character set by default.
    $this->connection->exec("SET NAMES 'UTF8'");

    // Execute PostgreSQL init_commands.
    if (isset($connection_options['init_commands'])) {
      $this->connection->exec(implode('; ', $connection_options['init_commands']));
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
