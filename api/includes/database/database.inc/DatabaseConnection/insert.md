# DatabaseConnection::insert()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 888–891 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L888-L891)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function insert($table, array $options = array())
```

## Documentation

```text
Prepares and returns an INSERT query object.

@param $options
  An array of options on the query.

@return InsertQuery
  A new InsertQuery object.

@see InsertQuery
```

## Code

```php
  public function insert($table, array $options = array()) {
    $class = $this->getDriverClass('InsertQuery', array('query.inc'));
    return new $class($this, $table, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
