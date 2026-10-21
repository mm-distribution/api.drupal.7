# Database::getConnectionInfo()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1699–1707 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1699-L1707)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function getConnectionInfo($key = 'default')
```

## Documentation

```text
Gets information on the specified database connection.

@param $connection
  The connection key for which we want information.
```

## Code

```php
  final public static function getConnectionInfo($key = 'default') {
    if (empty(self::$databaseInfo)) {
      self::parseConnectionInfo();
    }

    if (!empty(self::$databaseInfo[$key])) {
      return self::$databaseInfo[$key];
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
