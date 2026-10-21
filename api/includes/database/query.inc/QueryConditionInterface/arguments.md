# QueryConditionInterface::arguments()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 137–137 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L137)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function arguments();
```

## Documentation

```text
Gets a complete list of all values to insert into the prepared statement.

@return
  An associative array of placeholders and values.
```

## Code

```php
  public function arguments();
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
