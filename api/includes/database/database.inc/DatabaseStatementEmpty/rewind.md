# DatabaseStatementEmpty::rewind()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2414–2416 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2414-L2416)
- **Class:** [DatabaseStatementEmpty](../DatabaseStatementEmpty.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rewind()
```

## Documentation

_No docblock in source._

## Code

```php
  public function rewind() {
    // Nothing to do: our DatabaseStatement can't be rewound.
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
