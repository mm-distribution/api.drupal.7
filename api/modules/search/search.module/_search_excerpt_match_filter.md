# _search_excerpt_match_filter()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1342–1344 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1342-L1344)
- **Module/theme:** search

## Signature

```php
function _search_excerpt_match_filter($var)
```

## Documentation

```text
Helper function for array_filter() in search_search_excerpt_match().
```

## Code

```php
function _search_excerpt_match_filter($var) {
  return strlen(trim($var[0]));
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
