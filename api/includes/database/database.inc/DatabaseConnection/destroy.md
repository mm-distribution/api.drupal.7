# DatabaseConnection::destroy()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 364–372 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L364-L372)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function destroy()
```

## Documentation

```text
Destroys this Connection object.

PHP does not destruct an object if it is still referenced in other
variables. In case of PDO database connection objects, PHP only closes the
connection when the PDO object is destructed, so any references to this
object may cause the number of maximum allowed connections to be exceeded.
```

## Code

```php
  public function destroy() {
    // Destroy all references to this connection by setting them to NULL.
    // The Statement class attribute only accepts a new value that presents a
    // proper callable, so we reset it to PDOStatement.
    if (!empty($this->statementClass)) {
      $this->connection->setAttribute(PDO::ATTR_STATEMENT_CLASS, array('PDOStatement', array()));
    }
    $this->schema = NULL;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
