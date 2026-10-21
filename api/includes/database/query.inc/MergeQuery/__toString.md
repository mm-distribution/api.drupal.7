# MergeQuery::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1636–1637 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1636-L1637)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

```text
Implements PHP magic __toString method to convert the query to a string.

In the degenerate case, there is no string-able query as this operation
is potentially two queries.

@return string
  The prepared query statement.
```

## Code

```php
  public function __toString() {
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
