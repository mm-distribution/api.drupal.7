# Database::closeConnection()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1818–1843 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1818-L1843)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public static function closeConnection($target = NULL, $key = NULL)
```

## Documentation

```text
Closes a connection to the server specified by the given key and target.

@param $target
  The database target name.  Defaults to NULL meaning that all target
  connections will be closed.
@param $key
  The database connection key. Defaults to NULL which means the active key.
```

## Code

```php
  public static function closeConnection($target = NULL, $key = NULL) {
    // Gets the active connection by default.
    if (!isset($key)) {
      $key = self::$activeKey;
    }
    // To close a connection, it needs to be set to NULL and removed from the
    // static variable. In all cases, closeConnection() might be called for a
    // connection that was not opened yet, in which case the key is not defined
    // yet and we just ensure that the connection key is undefined.
    if (isset($target)) {
      if (isset(self::$connections[$key][$target])) {
        self::$connections[$key][$target]->destroy();
        self::$connections[$key][$target] = NULL;
      }
      unset(self::$connections[$key][$target]);
    }
    else {
      if (isset(self::$connections[$key])) {
        foreach (self::$connections[$key] as $target => $connection) {
          self::$connections[$key][$target]->destroy();
          self::$connections[$key][$target] = NULL;
        }
      }
      unset(self::$connections[$key]);
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
