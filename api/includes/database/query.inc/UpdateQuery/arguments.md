# UpdateQuery::arguments()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1084–1086 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1084-L1086)
- **Class:** [UpdateQuery](../UpdateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function arguments()
```

## Documentation

```text
Implements QueryConditionInterface::arguments().
```

## Code

```php
  public function arguments() {
    return $this->condition->arguments();
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
