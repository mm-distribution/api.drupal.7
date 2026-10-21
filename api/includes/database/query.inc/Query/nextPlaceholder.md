# Query::nextPlaceholder()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 392–394 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L392-L394)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function nextPlaceholder()
```

## Documentation

```text
Gets the next placeholder value for this query object.

@return int
  Next placeholder value.
```

## Code

```php
  public function nextPlaceholder() {
    return $this->nextPlaceholder++;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
