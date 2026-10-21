# TruncateQuery::execute()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 938–940 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L938-L940)
- **Class:** [TruncateQuery](../TruncateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

```text
Executes the TRUNCATE query.

@return
  Return value is dependent on the database type.
```

## Code

```php
  public function execute() {
    return $this->connection->query((string) $this, array(), $this->queryOptions);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
