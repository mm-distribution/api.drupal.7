# DatabaseStatementPrefetch::fetchField()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 399–401 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L399-L401)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchField($index = 0)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchField($index = 0) {
    return $this->fetchColumn($index);
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
