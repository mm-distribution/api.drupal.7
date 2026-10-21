# _search_excerpt_replace()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1267–1269 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1267-L1269)
- **Module/theme:** search

## Signature

```php
function _search_excerpt_replace(&$text)
```

## Documentation

```text
Helper function for array_walk() in search_excerpt().
```

## Code

```php
function _search_excerpt_replace(&$text) {
  $text = preg_quote($text, '/');
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
