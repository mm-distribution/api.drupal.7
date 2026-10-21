# Query::__construct()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 330–338 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L330-L338)
- **Class:** [Query](../Query.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(DatabaseConnection $connection, $options)
```

## Documentation

```text
Constructs a Query object.

@param DatabaseConnection $connection
  Database connection object.
@param array $options
  Array of query options.
```

## Code

```php
  public function __construct(DatabaseConnection $connection, $options) {
    $this->uniqueIdentifier = uniqid('', TRUE);

    $this->connection = $connection;
    $this->connectionKey = $this->connection->getKey();
    $this->connectionTarget = $this->connection->getTarget();

    $this->queryOptions = $options;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
