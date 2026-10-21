# DatabaseConnection::delete()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 937–940 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L937-L940)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function delete($table, array $options = array())
```

## Documentation

```text
Prepares and returns a DELETE query object.

@param $options
  An array of options on the query.

@return DeleteQuery
  A new DeleteQuery object.

@see DeleteQuery
```

## Code

```php
  public function delete($table, array $options = array()) {
    $class = $this->getDriverClass('DeleteQuery', array('query.inc'));
    return new $class($this, $table, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
