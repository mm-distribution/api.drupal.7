# DatabaseLog::clear()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 91–93 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L91-L93)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function clear($logging_key)
```

## Documentation

```text
Empty the query log for the specified logging key.

This method does not stop logging, it simply clears the log. To stop
logging, use the end() method.

@param $logging_key
  The logging key to empty.
```

## Code

```php
  public function clear($logging_key) {
    $this->queryLog[$logging_key] = array();
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
