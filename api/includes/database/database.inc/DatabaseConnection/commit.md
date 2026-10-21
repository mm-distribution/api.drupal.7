# DatabaseConnection::commit()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1364–1366 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1364-L1366)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function commit()
```

## Documentation

```text
Throws an exception to deny direct access to transaction commits.

We do not want to allow users to commit transactions at any time, only
by destroying the transaction object or allowing it to go out of scope.
A direct commit bypasses all of the safety checks we've built on top of
PDO's transaction routines.

@throws DatabaseTransactionExplicitCommitNotAllowedException

@see DatabaseTransaction
```

## Code

```php
  public function commit() {
    throw new DatabaseTransactionExplicitCommitNotAllowedException();
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
