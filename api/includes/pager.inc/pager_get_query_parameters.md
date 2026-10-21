# pager_get_query_parameters()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 309–315 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L309-L315)

## Signature

```php
function pager_get_query_parameters()
```

## Documentation

```text
Compose a URL query parameter array for pager links.

@return
  A URL query parameter array that consists of all components of the current
  page request except for those pertaining to paging.
```

## Code

```php
function pager_get_query_parameters() {
  $query = &drupal_static(__FUNCTION__);
  if (!isset($query)) {
    $query = drupal_get_query_parameters($_GET, array('q', 'page'));
  }
  return $query;
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
