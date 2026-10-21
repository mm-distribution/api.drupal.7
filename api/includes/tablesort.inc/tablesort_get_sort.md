# tablesort_get_sort()

- **Type:** Function
- **File:** [`includes/tablesort.inc`](_file.md), lines 239–255 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L239-L255)

## Signature

```php
function tablesort_get_sort($headers)
```

## Documentation

```text
Determines the current sort direction.

@param $headers
  An array of column headers in the format described in theme_table().

@return
  The current sort direction ("asc" or "desc").
```

## Code

```php
function tablesort_get_sort($headers) {
  if (isset($_GET['sort'])) {
    return (strtolower($_GET['sort']) == 'desc') ? 'desc' : 'asc';
  }
  // The user has not specified a sort. Use the default for the currently sorted
  // header if specified; otherwise use "asc".
  else {
    // Find out which header is currently being sorted.
    $ts = tablesort_get_order($headers);
    foreach ($headers as $header) {
      if (is_array($header) && isset($header['data']) && $header['data'] == $ts['name'] && isset($header['sort'])) {
        return $header['sort'];
      }
    }
  }
  return 'asc';
}
```

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
