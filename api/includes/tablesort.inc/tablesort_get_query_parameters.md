# tablesort_get_query_parameters()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 189–191 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L189-L191)

## Signature

```php
function tablesort_get_query_parameters()
```

## Documentation

```text
Composes a URL query parameter array for table sorting links.

@return
  A URL query parameter array that consists of all components of the current
  page request except for those pertaining to table sorting.
```

## Code

```php
function tablesort_get_query_parameters() {
  return drupal_get_query_parameters($_GET, array('q', 'sort', 'order'));
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
