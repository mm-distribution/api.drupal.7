# Database::isActiveConnection()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1597–1599 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1597-L1599)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function isActiveConnection()
```

## Documentation

```text
Determines if there is an active connection.

Note that this method will return FALSE if no connection has been
established yet, even if one could be.

@return
  TRUE if there is at least one database connection established, FALSE
  otherwise.
```

## Code

```php
  final public static function isActiveConnection() {
    return !empty(self::$activeKey) && !empty(self::$connections) && !empty(self::$connections[self::$activeKey]);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
