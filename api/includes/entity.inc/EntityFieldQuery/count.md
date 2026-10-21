# EntityFieldQuery::count()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1009–1012 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1009-L1012)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function count()
```

## Documentation

```text
Sets the query to be a count query only.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function count() {
    $this->count = TRUE;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
