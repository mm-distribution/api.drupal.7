# DatabaseConnection_mysql::__construct()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 300–387 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L300-L387)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
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

    // MySQL never supports transactional DDL.
    $this->transactionalDDLSupport = FALSE;

    $this->connectionOptions = $connection_options;

    $charset = 'utf8';
    // Check if the charset is overridden to utf8mb4 in settings.php.
    if ($this->utf8mb4IsActive()) {
      $charset = 'utf8mb4';
    }

    // The DSN should use either a socket or a host/port.
    if (isset($connection_options['unix_socket'])) {
      $dsn = 'mysql:unix_socket=' . $connection_options['unix_socket'];
    }
    else {
      // Default to TCP connection on port 3306.
      $dsn = 'mysql:host=' . $connection_options['host'] . ';port=' . (empty($connection_options['port']) ? 3306 : $connection_options['port']);
    }
    // Character set is added to dsn to ensure PDO uses the proper character
    // set when escaping. This has security implications. See
    // https://www.drupal.org/node/1201452 for further discussion.
    $dsn .= ';charset=' . $charset;
    $dsn .= ';dbname=' . $connection_options['database'];
    // Allow PDO options to be overridden.
    $connection_options += array(
      'pdo' => array(),
    );
    $connection_options['pdo'] += array(
      // So we don't have to mess around with cursors and unbuffered queries by default.
      PDO::MYSQL_ATTR_USE_BUFFERED_QUERY => TRUE,
      // Because MySQL's prepared statements skip the query cache, because it's dumb.
      PDO::ATTR_EMULATE_PREPARES => TRUE,
      // Convert numeric values to strings when fetching. In PHP 8.1,
      // PDO::ATTR_EMULATE_PREPARES now behaves the same way as non emulated
      // prepares and returns integers. See https://externals.io/message/113294
      // for further discussion.
      PDO::ATTR_STRINGIFY_FETCHES => TRUE,
    );
    if (defined('PDO::MYSQL_ATTR_MULTI_STATEMENTS')) {
      // An added connection option in PHP 5.5.21+ to optionally limit SQL to a
      // single statement like mysqli.
      $connection_options['pdo'] += array(PDO::MYSQL_ATTR_MULTI_STATEMENTS => FALSE);
    }

    parent::__construct($dsn, $connection_options['username'], $connection_options['password'], $connection_options['pdo']);

    // Force MySQL to use the UTF-8 character set. Also set the collation, if a
    // certain one has been set; otherwise, MySQL defaults to 'utf8_general_ci'
    // for UTF-8.
    if (!empty($connection_options['collation'])) {
      $this->connection->exec('SET NAMES ' . $charset . ' COLLATE ' . $connection_options['collation']);
    }
    else {
      $this->connection->exec('SET NAMES ' . $charset);
    }

    // Set MySQL init_commands if not already defined.  Default Drupal's MySQL
    // behavior to conform more closely to SQL standards.  This allows Drupal
    // to run almost seamlessly on many different kinds of database systems.
    // These settings force MySQL to behave the same as postgresql, or sqlite
    // in regards to syntax interpretation and invalid data handling.  See
    // http://drupal.org/node/344575 for further discussion. Also, as MySQL 5.5
    // changed the meaning of TRADITIONAL we need to spell out the modes one by
    // one.
    $connection_options += array(
      'init_commands' => array(),
    );

    $sql_mode = 'REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO';
    // NO_AUTO_CREATE_USER was removed in MySQL 8.0.11
    // https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-11.html#mysqld-8-0-11-deprecation-removal
    if (version_compare($this->connection->getAttribute(PDO::ATTR_SERVER_VERSION), '8.0.11', '<')) {
      $sql_mode .= ',NO_AUTO_CREATE_USER';
    }
    $connection_options['init_commands'] += array(
      'sql_mode' => "SET sql_mode = '$sql_mode'",
    );

    // Execute initial commands.
    foreach ($connection_options['init_commands'] as $sql) {
      $this->connection->exec($sql);
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
