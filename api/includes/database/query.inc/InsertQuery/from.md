# InsertQuery::from()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 605–608 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L605-L608)
- **Class:** [InsertQuery](../InsertQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function from(SelectQueryInterface $query)
```

## Documentation

```text
Sets the fromQuery on this InsertQuery object.

@param SelectQueryInterface $query
  The query to fetch the rows that should be inserted.

@return InsertQuery
  The called object.
```

## Code

```php
  public function from(SelectQueryInterface $query) {
    $this->fromQuery = $query;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
