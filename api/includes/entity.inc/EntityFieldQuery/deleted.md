# EntityFieldQuery::deleted()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1107–1110 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1107-L1110)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function deleted($deleted = TRUE)
```

## Documentation

```text
Filters on the data being deleted.

@param $deleted
  TRUE to only return deleted data, FALSE to return non-deleted data,
  EntityFieldQuery::RETURN_ALL to return everything. Defaults to FALSE.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function deleted($deleted = TRUE) {
    $this->deleted = $deleted;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
