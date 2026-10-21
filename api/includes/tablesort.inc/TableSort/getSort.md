# TableSort::getSort()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 74–76 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L74-L76)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
protected function getSort()
```

## Documentation

```text
Determine the current sort direction.

@param $headers
  An array of column headers in the format described in theme_table().
@return
  The current sort direction ("asc" or "desc").
```

## Code

```php
  protected function getSort() {
    return tablesort_get_sort($this->header);
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
