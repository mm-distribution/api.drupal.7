# DatabaseConnection::truncate()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 953–956 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L953-L956)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function truncate($table, array $options = array())
```

## Documentation

```text
Prepares and returns a TRUNCATE query object.

@param $options
  An array of options on the query.

@return TruncateQuery
  A new TruncateQuery object.

@see TruncateQuery
```

## Code

```php
  public function truncate($table, array $options = array()) {
    $class = $this->getDriverClass('TruncateQuery', array('query.inc'));
    return new $class($this, $table, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
