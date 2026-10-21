# DatabaseConnection::update()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 921–924 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L921-L924)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function update($table, array $options = array())
```

## Documentation

```text
Prepares and returns an UPDATE query object.

@param $options
  An array of options on the query.

@return UpdateQuery
  A new UpdateQuery object.

@see UpdateQuery
```

## Code

```php
  public function update($table, array $options = array()) {
    $class = $this->getDriverClass('UpdateQuery', array('query.inc'));
    return new $class($this, $table, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
