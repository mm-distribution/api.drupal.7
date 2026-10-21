# PagerDefault::limit()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 137–140 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L137-L140)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function limit($limit = 10)
```

## Documentation

```text
Specify the maximum number of elements per page for this query.

The default if not specified is 10 items per page.

@param $limit
  An integer specifying the number of elements per page.  If passed a false
  value (FALSE, 0, NULL), the pager is disabled.
```

## Code

```php
  public function limit($limit = 10) {
    $this->limit = $limit;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
