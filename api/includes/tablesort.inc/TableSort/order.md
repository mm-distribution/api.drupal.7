# TableSort::order()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 101–103 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L101-L103)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
protected function order()
```

## Documentation

```text
Determine the current sort criterion.

@param $headers
  An array of column headers in the format described in theme_table().
@return
  An associative array describing the criterion, containing the keys:
  - "name": The localized title of the table column.
  - "sql": The name of the database field to sort on.
```

## Code

```php
  protected function order() {
    return tablesort_get_order($this->header);
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
