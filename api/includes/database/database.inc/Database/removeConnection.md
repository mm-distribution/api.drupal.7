# Database::removeConnection()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1752–1763 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1752-L1763)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function removeConnection($key, $close = TRUE)
```

## Documentation

```text
Remove a connection and its corresponding connection information.

@param $key
  The connection key.
@param $close
  Whether to close the connection.
@return
  TRUE in case of success, FALSE otherwise.
```

## Code

```php
  final public static function removeConnection($key, $close = TRUE) {
    if (isset(self::$databaseInfo[$key])) {
      if ($close) {
        self::closeConnection(NULL, $key);
      }
      unset(self::$databaseInfo[$key]);
      return TRUE;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
