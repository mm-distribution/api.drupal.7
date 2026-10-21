# DatabaseStatementInterface::fetchAssoc()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2168–2168 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2168)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAssoc();
```

## Documentation

```text
Fetches the next row and returns it as an associative array.

This method corresponds to PDOStatement::fetchObject(), but for associative
arrays. For some reason PDOStatement does not have a corresponding array
helper method, so one is added.

@return
  An associative array, or FALSE if there is no next row.
```

## Code

```php
  public function fetchAssoc();
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
