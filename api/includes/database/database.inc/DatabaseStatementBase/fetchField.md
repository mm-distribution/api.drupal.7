# DatabaseStatementBase::fetchField()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2330–2333 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2330-L2333)
- **Class:** [DatabaseStatementBase](../DatabaseStatementBase.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchField($index = 0)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchField($index = 0) {
    // Call PDOStatement::fetchColumn to fetch the field.
    return $this->fetchColumn($index);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
