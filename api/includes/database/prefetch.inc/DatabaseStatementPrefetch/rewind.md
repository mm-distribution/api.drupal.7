# DatabaseStatementPrefetch::rewind()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 339–341 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L339-L341)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rewind()
```

## Documentation

_No docblock in source._

## Code

```php
  public function rewind() {
    // Nothing to do: our DatabaseStatement can't be rewound.
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
