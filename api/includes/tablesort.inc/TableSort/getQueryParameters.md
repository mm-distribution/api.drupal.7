# TableSort::getQueryParameters()

- **Type:** Method
- **File:** [`includes/tablesort.inc`](../_file.md), lines 87–89 · [local source](../../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L87-L89)
- **Class:** [TableSort](../TableSort.md)

## Signature

```php
protected function getQueryParameters()
```

## Documentation

```text
Compose a URL query parameter array to append to table sorting requests.

@return
  A URL query parameter array that consists of all components of the current
  page request except for those pertaining to table sorting.

@see tablesort_get_query_parameters()
```

## Code

```php
  protected function getQueryParameters() {
    return tablesort_get_query_parameters();
  }
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
