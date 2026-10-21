# Database::getConnection()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1566–1585 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1566-L1585)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function getConnection($target = 'default', $key = NULL)
```

## Documentation

```text
Gets the connection object for the specified database key and target.

@param $target
  The database target name.
@param $key
  The database connection key. Defaults to NULL which means the active key.

@return DatabaseConnection
  The corresponding connection object.
```

## Code

```php
  final public static function getConnection($target = 'default', $key = NULL) {
    if (!isset($key)) {
      // By default, we want the active connection, set in setActiveConnection.
      $key = self::$activeKey;
    }
    // If the requested target does not exist, or if it is ignored, we fall back
    // to the default target. The target is typically either "default" or
    // "slave", indicating to use a slave SQL server if one is available. If
    // it's not available, then the default/master server is the correct server
    // to use.
    if (!empty(self::$ignoreTargets[$key][$target]) || !isset(self::$databaseInfo[$key][$target])) {
      $target = 'default';
    }

    if (!isset(self::$connections[$key][$target])) {
      // If necessary, a new connection is opened.
      self::$connections[$key][$target] = self::openConnection($key, $target);
    }
    return self::$connections[$key][$target];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
