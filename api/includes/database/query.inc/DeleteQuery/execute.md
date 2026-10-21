# DeleteQuery::execute()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 851–859 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L851-L859)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

```text
Executes the DELETE query.

@return int
  The number of rows affected by the delete query.
```

## Code

```php
  public function execute() {
    $values = array();
    if (count($this->condition)) {
      $this->condition->compile($this->connection, $this);
      $values = $this->condition->arguments();
    }

    return $this->connection->query((string) $this, $values, $this->queryOptions);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
