# MergeQuery::arguments()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1601–1603 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1601-L1603)
- **Class:** [MergeQuery](../MergeQuery.md)
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
