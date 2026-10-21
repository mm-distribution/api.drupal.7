# PagerDefault::getCountQuery()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 119–126 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L119-L126)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function getCountQuery()
```

## Documentation

```text
Retrieve the count query for this pager.

The count query may be specified manually or, by default, taken from the
query we are extending.

@return SelectQueryInterface
  A count query object.
```

## Code

```php
  public function getCountQuery() {
    if ($this->customCountQuery) {
      return $this->customCountQuery;
    }
    else {
      return $this->query->countQuery();
    }
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
