# search_expression_extract()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 871–875 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L871-L875)
- **Module/theme:** search

## Signature

```php
function search_expression_extract($expression, $option)
```

## Documentation

```text
Extracts a module-specific search option from a search expression.

Search options are added using search_expression_insert(), and retrieved
using search_expression_extract(). They take the form option:value, and
are added to the ordinary keywords in the search expression.

@param $expression
  The search expression to extract from.
@param $option
  The name of the option to retrieve from the search expression.

@return
  The value previously stored in the search expression for option $option,
  if any. Trailing spaces in values will not be included.
```

## Code

```php
function search_expression_extract($expression, $option) {
  if (preg_match('/(^| )' . $option . ':([^ ]*)( |$)/i', $expression, $matches)) {
    return $matches[2];
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
