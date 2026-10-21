# SelectQueryExtender::__construct()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 562–566 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L562-L566)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(SelectQueryInterface $query, DatabaseConnection $connection)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct(SelectQueryInterface $query, DatabaseConnection $connection) {
    $this->uniqueIdentifier = uniqid('', TRUE);
    $this->query = $query;
    $this->connection = $connection;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
