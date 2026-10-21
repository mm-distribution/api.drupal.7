# SelectQuery_pgsql::orderRandom()

- **Type:** Method
- **File:** [`includes/database/pgsql/select.inc`](../_file.md), lines 15–19 · [local source](../../../../../../source/includes/database/pgsql/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/select.inc#L15-L19)
- **Class:** [SelectQuery_pgsql](../SelectQuery_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function orderRandom()
```

## Documentation

_No docblock in source._

## Code

```php
  public function orderRandom() {
    $alias = $this->addExpression('RANDOM()', 'random_field');
    $this->orderBy($alias);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
