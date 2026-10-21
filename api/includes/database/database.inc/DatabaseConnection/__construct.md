# DatabaseConnection::__construct()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 327–341 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L327-L341)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
function __construct($dsn, $username, $password, $driver_options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  function __construct($dsn, $username, $password, $driver_options = array()) {
    // Initialize and prepare the connection prefix.
    $this->setPrefix(isset($this->connectionOptions['prefix']) ? $this->connectionOptions['prefix'] : '');

    // Because the other methods don't seem to work right.
    $driver_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;

    // Call PDO::__construct and PDO::setAttribute.
    $this->connection = new PDO($dsn, $username, $password, $driver_options);

    // Set a Statement class, unless the driver opted out.
    if (!empty($this->statementClass)) {
      $this->connection->setAttribute(PDO::ATTR_STATEMENT_CLASS, array($this->statementClass, array($this)));
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
