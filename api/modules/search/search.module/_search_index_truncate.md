# _search_index_truncate()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 525–530 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L525-L530)
- **Module/theme:** search

## Signature

```php
function _search_index_truncate(&$text)
```

## Documentation

```text
Helper function for array_walk in search_index_split.
```

## Code

```php
function _search_index_truncate(&$text) {
  if (is_numeric($text)) {
    $text = ltrim($text, '0');
  }
  $text = truncate_utf8($text, 50);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
