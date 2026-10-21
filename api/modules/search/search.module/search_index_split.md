# search_index_split()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 504–520 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L504-L520)
- **Module/theme:** search

## Signature

```php
function search_index_split($text)
```

## Documentation

```text
Simplifies and splits a string into tokens for indexing.
```

## Code

```php
function search_index_split($text) {
  $last = &drupal_static(__FUNCTION__);
  $lastsplit = &drupal_static(__FUNCTION__ . ':lastsplit');

  if ($last == $text) {
    return $lastsplit;
  }
  // Process words
  $text = search_simplify($text);
  $words = explode(' ', $text);

  // Save last keyword result
  $last = $text;
  $lastsplit = $words;

  return $words;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
