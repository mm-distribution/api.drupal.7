# DatabaseLog::get()

- **Type:** Method
- **File:** [`includes/database/log.inc`](../_file.md), lines 78–80 · [local source](../../../../../source/includes/database/log.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc#L78-L80)
- **Class:** [DatabaseLog](../DatabaseLog.md)

## Signature

```php
public function get($logging_key)
```

## Documentation

```text
Retrieve the query log for the specified logging key so far.

@param $logging_key
  The logging key to fetch.
@return
  An indexed array of all query records for this logging key.
```

## Code

```php
  public function get($logging_key) {
    return $this->queryLog[$logging_key];
  }
```

---
_Drupal 7.103 · [includes/database/log.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/log.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
