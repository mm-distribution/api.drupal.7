# DatabaseStatementPrefetch::valid()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 356–358 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L356-L358)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function valid()
```

## Documentation

_No docblock in source._

## Code

```php
  public function valid() {
    return isset($this->currentRow);
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
