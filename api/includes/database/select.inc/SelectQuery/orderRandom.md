# SelectQuery::orderRandom()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1440–1444 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1440-L1444)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function orderRandom()
```

## Documentation

_No docblock in source._

## Code

```php
  public function orderRandom() {
    $alias = $this->addExpression('RAND()', 'random_field');
    $this->orderBy($alias);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
