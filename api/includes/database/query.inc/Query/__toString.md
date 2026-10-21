# Query::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 377–377 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L377)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract public function __toString();
```

## Documentation

```text
Implements PHP magic __toString method to convert the query to a string.

The toString operation is how we compile a query object to a prepared
statement.

@return
  A prepared statement query string for this object.
```

## Code

```php
  abstract public function __toString();
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
