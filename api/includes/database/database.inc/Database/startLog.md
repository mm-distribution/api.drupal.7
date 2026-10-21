# Database::startLog()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1511–1526 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1511-L1526)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function startLog($logging_key, $key = 'default')
```

## Documentation

```text
Starts logging a given logging key on the specified connection.

@param $logging_key
  The logging key to log.
@param $key
  The database connection key for which we want to log.

@return DatabaseLog
  The query log object. Note that the log object does support richer
  methods than the few exposed through the Database class, so in some
  cases it may be desirable to access it directly.

@see DatabaseLog
```

## Code

```php
  final public static function startLog($logging_key, $key = 'default') {
    if (empty(self::$logs[$key])) {
      self::$logs[$key] = new DatabaseLog($key);

      // Every target already active for this connection key needs to have the
      // logging object associated with it.
      if (!empty(self::$connections[$key])) {
        foreach (self::$connections[$key] as $connection) {
          $connection->setLogger(self::$logs[$key]);
        }
      }
    }

    self::$logs[$key]->start($logging_key);
    return self::$logs[$key];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
