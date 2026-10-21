# DatabaseStatementBase::__construct()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2260–2263 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2260-L2263)
- **Class:** [DatabaseStatementBase](../DatabaseStatementBase.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function __construct($dbh)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function __construct($dbh) {
    $this->dbh = $dbh;
    $this->setFetchMode(PDO::FETCH_OBJ);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
