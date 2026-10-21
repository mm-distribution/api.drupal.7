# DatabaseLog::end()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 101–103 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L101-L103)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function end($logging_key)
```

## Documentation

```text
Stop logging for the specified logging key.

@param $logging_key
  The logging key to stop.
```

## Code

```php
  public function end($logging_key) {
    unset($this->queryLog[$logging_key]);
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
