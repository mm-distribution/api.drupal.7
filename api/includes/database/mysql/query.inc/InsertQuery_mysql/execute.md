# InsertQuery_mysql::execute()

- **Type:** Method
- **File:** [`includes/database/mysql/query.inc`](../_file.md), lines 16–42 · [local source](../../../../../../source/includes/database/mysql/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/query.inc#L16-L42)
- **Class:** [InsertQuery_mysql](../InsertQuery_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute() {
    if (!$this->preExecute()) {
      return NULL;
    }

    // If we're selecting from a SelectQuery, finish building the query and
    // pass it back, as any remaining options are irrelevant.
    if (empty($this->fromQuery)) {
      $max_placeholder = 0;
      $values = array();
      foreach ($this->insertValues as $insert_values) {
        foreach ($insert_values as $value) {
          $values[':db_insert_placeholder_' . $max_placeholder++] = $value;
        }
      }
    }
    else {
      $values = $this->fromQuery->getArguments();
    }

    $last_insert_id = $this->connection->query((string) $this, $values, $this->queryOptions);

    // Re-initialize the values array so that we can re-use this query.
    $this->insertValues = array();

    return $last_insert_id;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
