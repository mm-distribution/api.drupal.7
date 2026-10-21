# DatabaseStatementInterface::fetchCol()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2196–2196 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2196)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchCol($index = 0);
```

## Documentation

```text
Returns an entire single column of a result set as an indexed array.

Note that this method will run the result set to the end.

@param $index
  The index of the column number to fetch.

@return
  An indexed array, or an empty array if there is no result set.
```

## Code

```php
  public function fetchCol($index = 0);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
