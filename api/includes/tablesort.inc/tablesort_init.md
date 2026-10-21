# tablesort_init()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 109–114 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L109-L114)

## Signature

```php
function tablesort_init($header)
```

## Documentation

```text
Initialize the table sort context.
```

## Code

```php
function tablesort_init($header) {
  $ts = tablesort_get_order($header);
  $ts['sort'] = tablesort_get_sort($header);
  $ts['query'] = tablesort_get_query_parameters();
  return $ts;
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
