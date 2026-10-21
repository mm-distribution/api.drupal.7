# DatabaseStatementPrefetch::rowCount()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 362–364 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L362-L364)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rowCount()
```

## Documentation

_No docblock in source._

## Code

```php
  public function rowCount() {
    return $this->rowCount;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
