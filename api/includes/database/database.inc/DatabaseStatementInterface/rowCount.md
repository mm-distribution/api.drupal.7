# DatabaseStatementInterface::rowCount()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2099–2099 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2099)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rowCount();
```

## Documentation

```text
Returns the number of rows affected by the last SQL statement.

@return
  The number of rows affected by the last DELETE, INSERT, or UPDATE
  statement executed.
```

## Code

```php
  public function rowCount();
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
