# search_dirty()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 339–347 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L339-L347)
- **Module/theme:** search

## Signature

```php
function search_dirty($word = NULL)
```

## Documentation

```text
Marks a word as "dirty" (changed), or retrieves the list of dirty words.

This is used during indexing (cron). Words that are dirty have outdated
total counts in the search_total table, and need to be recounted.
```

## Code

```php
function search_dirty($word = NULL) {
  $dirty = &drupal_static(__FUNCTION__, array());
  if ($word !== NULL) {
    $dirty[$word] = TRUE;
  }
  else {
    return $dirty;
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
