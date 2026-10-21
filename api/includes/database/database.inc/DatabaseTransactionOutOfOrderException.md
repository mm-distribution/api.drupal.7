# DatabaseTransactionOutOfOrderException

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1917–1917 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1917)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseTransactionOutOfOrderException extends Exception { }
```

## Documentation

```text
Exception thrown when a rollback() resulted in other active transactions being rolled-back.
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
