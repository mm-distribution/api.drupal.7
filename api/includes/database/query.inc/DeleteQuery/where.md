# DeleteQuery::where()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 826–829 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L826-L829)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function where($snippet, $args = array())
```

## Documentation

```text
Implements QueryConditionInterface::where().
```

## Code

```php
  public function where($snippet, $args = array()) {
    $this->condition->where($snippet, $args);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
