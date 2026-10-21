# DatabaseLog::start()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 64–68 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L64-L68)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function start($logging_key)
```

## Documentation

```text
Begin logging queries to the specified connection and logging key.

If the specified logging key is already running this method does nothing.

@param $logging_key
  The identification key for this log request. By specifying different
  logging keys we are able to start and stop multiple logging runs
  simultaneously without them colliding.
```

## Code

```php
  public function start($logging_key) {
    if (empty($this->queryLog[$logging_key])) {
      $this->clear($logging_key);
    }
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
