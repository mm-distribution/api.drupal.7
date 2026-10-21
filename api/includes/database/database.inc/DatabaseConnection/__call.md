# DatabaseConnection::__call()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 352–354 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L352-L354)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __call($name, $arguments)
```

## Documentation

```text
Proxy possible direct calls to the \PDO methods.

Since PHP8.0 the signature of the the \PDO::query() method has changed,
and this class can't extending \PDO any more.

However, for the BC, proxy any calls to the \PDO methods to the actual
PDO connection object.
```

## Code

```php
  public function __call($name, $arguments) {
    return call_user_func_array(array($this->connection, $name), $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
