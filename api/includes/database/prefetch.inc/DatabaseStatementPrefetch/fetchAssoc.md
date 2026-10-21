# DatabaseStatementPrefetch::fetchAssoc()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 428–437 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L428-L437)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAssoc()
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAssoc() {
    if (isset($this->currentRow)) {
      $result = $this->currentRow;
      $this->next();
      return $result;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
