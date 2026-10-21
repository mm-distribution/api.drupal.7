# DatabaseStatementInterface::fetchField()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2148–2148 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2148)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchField($index = 0);
```

## Documentation

```text
Returns a single field from the next record of a result set.

@param $index
  The numeric index of the field to return. Defaults to the first field.

@return
  A single field from the next record, or FALSE if there is no next record.
```

## Code

```php
  public function fetchField($index = 0);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
