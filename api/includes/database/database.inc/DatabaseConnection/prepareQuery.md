# DatabaseConnection::prepareQuery()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 540–545 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L540-L545)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function prepareQuery($query)
```

## Documentation

```text
Prepares a query string and returns the prepared statement.

This method caches prepared statements, reusing them when
possible. It also prefixes tables names enclosed in curly-braces.

@param $query
  The query string as SQL, with curly-braces surrounding the
  table names.

@return DatabaseStatementInterface
  A PDO prepared statement ready for its execute() method.
```

## Code

```php
  public function prepareQuery($query) {
    $query = $this->prefixTables($query);

    // Call PDO::prepare.
    return $this->connection->prepare($query);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
