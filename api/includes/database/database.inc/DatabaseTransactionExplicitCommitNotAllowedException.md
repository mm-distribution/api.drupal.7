# DatabaseTransactionExplicitCommitNotAllowedException

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1912–1912 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1912)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseTransactionExplicitCommitNotAllowedException extends Exception { }
```

## Documentation

```text
Exception to deny attempts to explicitly manage transactions.

This exception will be thrown when the PDO connection commit() is called.
Code should never call this method directly.
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
