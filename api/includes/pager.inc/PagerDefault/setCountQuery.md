# PagerDefault::setCountQuery()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 106–108 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L106-L108)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function setCountQuery(SelectQueryInterface $query)
```

## Documentation

```text
Specify the count query object to use for this pager.

You will rarely need to specify a count query directly.  If not specified,
one is generated off of the pager query itself.

@param SelectQueryInterface $query
  The count query object.  It must return a single row with a single column,
  which is the total number of records.
```

## Code

```php
  public function setCountQuery(SelectQueryInterface $query) {
    $this->customCountQuery = $query;
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
