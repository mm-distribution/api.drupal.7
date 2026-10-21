# DatabaseLog::__construct()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 50–52 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L50-L52)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function __construct($key = 'default')
```

## Documentation

```text
Constructor.

@param $key
  The database connection key for which to enable logging.
```

## Code

```php
  public function __construct($key = 'default') {
    $this->connectionKey = $key;
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
