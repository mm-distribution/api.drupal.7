# DatabaseLog

- **Type:** Class
- **File:** [`includes/database/log.inc`](_file.md), lines 19–161 · [local source](../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L19-L161)

## Signature

```php
class DatabaseLog
```

## Documentation

```text
Database query logger.

We log queries in a separate object rather than in the connection object
because we want to be able to see all queries sent to a given database, not
database target. If we logged the queries in each connection object we
would not be able to track what queries went to which target.

Every connection has one and only one logging object on it for all targets
and logging keys.
```

## Properties

### $queryLog

```php
protected $queryLog = array();
```

```text
Cache of logged queries. This will only be used if the query logger is enabled.

The structure for the logging array is as follows:

array(
  $logging_key = array(
    array(query => '', args => array(), caller => '', target => '', time => 0),
    array(query => '', args => array(), caller => '', target => '', time => 0),
  ),
);

@var array
```

### $connectionKey

```php
protected $connectionKey = 'default';
```

```text
The connection key for which this object is logging.

@var string
```

## Methods (derived index)

- [__construct()](DatabaseLog/__construct.md) — Constructor.
- [start()](DatabaseLog/start.md) — Begin logging queries to the specified connection and logging key.
- [get()](DatabaseLog/get.md) — Retrieve the query log for the specified logging key so far.
- [clear()](DatabaseLog/clear.md) — Empty the query log for the specified logging key.
- [end()](DatabaseLog/end.md) — Stop logging for the specified logging key.
- [log()](DatabaseLog/log.md) — Log a query to all active logging keys.
- [findCaller()](DatabaseLog/findCaller.md) — Determine the routine that called this query.

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
