# DatabaseStatementBase::getQueryString()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2294–2296 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2294-L2296)
- **Class:** [DatabaseStatementBase](../DatabaseStatementBase.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getQueryString()
```

## Documentation

_No docblock in source._

## Code

```php
  public function getQueryString() {
    return $this->queryString;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
