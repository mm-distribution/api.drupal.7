# InvalidMergeQueryException

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1925–1925 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1925)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class InvalidMergeQueryException extends Exception {}
```

## Documentation

```text
Exception thrown for merge queries that do not make semantic sense.

There are many ways that a merge query could be malformed.  They should all
throw this exception and set an appropriately descriptive message.
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
