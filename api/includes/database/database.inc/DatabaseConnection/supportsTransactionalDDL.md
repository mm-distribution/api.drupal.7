# DatabaseConnection::supportsTransactionalDDL()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1324–1326 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1324-L1326)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function supportsTransactionalDDL()
```

## Documentation

```text
Determines if this driver supports transactional DDL.

DDL queries are those that change the schema, such as ALTER queries.

@return
  TRUE if this connection supports transactions for DDL queries, FALSE
  otherwise.
```

## Code

```php
  public function supportsTransactionalDDL() {
    return $this->transactionalDDLSupport;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
