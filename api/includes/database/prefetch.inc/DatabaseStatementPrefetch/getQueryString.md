# DatabaseStatementPrefetch::getQueryString()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 232–234 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L232-L234)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getQueryString()
```

## Documentation

```text
Return the object's SQL query string.
```

## Code

```php
  public function getQueryString() {
    return $this->queryString;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
