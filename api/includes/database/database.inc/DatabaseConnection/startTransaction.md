# DatabaseConnection::startTransaction()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1085–1088 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1085-L1088)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function startTransaction($name = '')
```

## Documentation

```text
Returns a new DatabaseTransaction object on this connection.

@param $name
  Optional name of the savepoint.

@return DatabaseTransaction
  A DatabaseTransaction object.

@see DatabaseTransaction
```

## Code

```php
  public function startTransaction($name = '') {
    $class = $this->getDriverClass('DatabaseTransaction');
    return new $class($this, $name);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
