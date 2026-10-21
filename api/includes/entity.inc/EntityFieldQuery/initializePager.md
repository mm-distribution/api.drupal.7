# EntityFieldQuery::initializePager()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1355–1364 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1355-L1364)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
function initializePager()
```

## Documentation

```text
Gets the total number of results and initializes a pager for the query.

The pager can be disabled by either setting the pager limit to 0, or by
setting this query to be a count query.
```

## Code

```php
  function initializePager() {
    if ($this->pager && !empty($this->pager['limit']) && !$this->count) {
      $page = pager_find_page($this->pager['element']);
      $count_query = clone $this;
      $this->pager['total'] = $count_query->count()->execute();
      $this->pager['start'] = $page * $this->pager['limit'];
      pager_default_initialize($this->pager['total'], $this->pager['limit'], $this->pager['element']);
      $this->range($this->pager['start'], $this->pager['limit']);
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
