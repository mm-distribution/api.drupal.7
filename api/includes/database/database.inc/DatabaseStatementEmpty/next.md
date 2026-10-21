# DatabaseStatementEmpty::next()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2419–2421 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2419-L2421)
- **Class:** [DatabaseStatementEmpty](../DatabaseStatementEmpty.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function next()
```

## Documentation

_No docblock in source._

## Code

```php
  public function next() {
    // Do nothing, since this is an always-empty implementation.
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
