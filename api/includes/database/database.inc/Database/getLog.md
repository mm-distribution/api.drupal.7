# Database::getLog()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1546–1553 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1546-L1553)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function getLog($logging_key, $key = 'default')
```

## Documentation

```text
Retrieves the queries logged on for given logging key.

This method also ends logging for the specified key. To get the query log
to date without ending the logger request the logging object by starting
it again (which does nothing to an open log key) and call methods on it as
desired.

@param $logging_key
  The logging key to log.
@param $key
  The database connection key for which we want to log.

@return array
  The query log for the specified logging key and connection.

@see DatabaseLog
```

## Code

```php
  final public static function getLog($logging_key, $key = 'default') {
    if (empty(self::$logs[$key])) {
      return NULL;
    }
    $queries = self::$logs[$key]->get($logging_key);
    self::$logs[$key]->end($logging_key);
    return $queries;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
