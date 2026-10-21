# DatabaseLog::log()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 115–125 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L115-L125)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function log(DatabaseStatementInterface $statement, $args, $time)
```

## Documentation

```text
Log a query to all active logging keys.

@param $statement
  The prepared statement object to log.
@param $args
  The arguments passed to the statement object.
@param $time
  The time in milliseconds the query took to execute.
```

## Code

```php
  public function log(DatabaseStatementInterface $statement, $args, $time) {
    foreach (array_keys($this->queryLog) as $key) {
      $this->queryLog[$key][] = array(
        'query' => $statement->getQueryString(),
        'args' => $args,
        'target' => $statement->dbh->getTarget(),
        'caller' => $this->findCaller(),
        'time' => $time,
      );
    }
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
