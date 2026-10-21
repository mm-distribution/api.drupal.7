# Database::openConnection()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1777–1807 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1777-L1807)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final protected static function openConnection($key, $target)
```

## Documentation

```text
Opens a connection to the server specified by the given key and target.

@param $key
  The database connection key, as specified in settings.php. The default is
  "default".
@param $target
  The database target to open.

@throws DatabaseConnectionNotDefinedException
@throws DatabaseDriverNotSpecifiedException
```

## Code

```php
  final protected static function openConnection($key, $target) {
    if (empty(self::$databaseInfo)) {
      self::parseConnectionInfo();
    }

    // If the requested database does not exist then it is an unrecoverable
    // error.
    if (!isset(self::$databaseInfo[$key])) {
      throw new DatabaseConnectionNotDefinedException('The specified database connection is not defined: ' . $key);
    }

    if (!$driver = self::$databaseInfo[$key][$target]['driver']) {
      throw new DatabaseDriverNotSpecifiedException('Driver not specified for this database connection: ' . $key);
    }

    // We cannot rely on the registry yet, because the registry requires an
    // open database connection.
    $driver_class = 'DatabaseConnection_' . $driver;
    require_once DRUPAL_ROOT . '/includes/database/' . $driver . '/database.inc';
    $new_connection = new $driver_class(self::$databaseInfo[$key][$target]);
    $new_connection->setTarget($target);
    $new_connection->setKey($key);

    // If we have any active logging objects for this connection key, we need
    // to associate them with the connection we just opened.
    if (!empty(self::$logs[$key])) {
      $new_connection->setLogger(self::$logs[$key]);
    }

    return $new_connection;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
