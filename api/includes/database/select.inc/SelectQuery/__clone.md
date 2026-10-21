# SelectQuery::__clone()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1657–1674 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1657-L1674)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __clone()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __clone() {
    parent::__clone();

    // On cloning, also clone the dependent objects. However, we do not
    // want to clone the database connection object as that would duplicate the
    // connection itself.

    $this->where = clone($this->where);
    $this->having = clone($this->having);
    foreach ($this->union as $key => $aggregate) {
      $this->union[$key]['query'] = clone($aggregate['query']);
    }
    foreach ($this->tables as $alias => $table) {
      if ($table['table'] instanceof SelectQueryInterface) {
        $this->tables[$alias]['table'] = clone $table['table'];
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
