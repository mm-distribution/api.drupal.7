# DatabaseConnection::merge()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 904–907 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L904-L907)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function merge($table, array $options = array())
```

## Documentation

```text
Prepares and returns a MERGE query object.

@param $options
  An array of options on the query.

@return MergeQuery
  A new MergeQuery object.

@see MergeQuery
```

## Code

```php
  public function merge($table, array $options = array()) {
    $class = $this->getDriverClass('MergeQuery', array('query.inc'));
    return new $class($this, $table, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
