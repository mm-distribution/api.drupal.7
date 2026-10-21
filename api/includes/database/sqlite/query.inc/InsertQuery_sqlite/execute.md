# InsertQuery_sqlite::execute()

- **Type:** Method
- **File:** [`includes/database/sqlite/query.inc`](../_file.md), lines 22–32 · [local source](../../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L22-L32)
- **Class:** [InsertQuery_sqlite](../InsertQuery_sqlite.md)
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
    if (count($this->insertFields) || !empty($this->fromQuery)) {
      return parent::execute();
    }
    else {
      return $this->connection->query('INSERT INTO {' . $this->table . '} DEFAULT VALUES', array(), $this->queryOptions);
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
