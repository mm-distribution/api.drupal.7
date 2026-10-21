# DatabaseStatementEmpty::fetchCol()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2390–2392 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2390-L2392)
- **Class:** [DatabaseStatementEmpty](../DatabaseStatementEmpty.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchCol($index = 0)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchCol($index = 0) {
    return array();
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
