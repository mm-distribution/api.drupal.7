# search_expression_insert()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 900–909 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L900-L909)
- **Module/theme:** search

## Signature

```php
function search_expression_insert($expression, $option, $value = NULL)
```

## Documentation

```text
Adds a module-specific search option to a search expression.

Search options are added using search_expression_insert(), and retrieved
using search_expression_extract(). They take the form option:value, and
are added to the ordinary keywords in the search expression.

@param $expression
  The search expression to add to.
@param $option
  The name of the option to add to the search expression.
@param $value
  The value to add for the option. If present, it will replace any previous
  value added for the option. Cannot contain any spaces or | characters, as
  these are used as delimiters. If you want to add a blank value $option: to
  the search expression, pass in an empty string or a string that is composed
  of only spaces. To clear a previously-stored option without adding a
  replacement, pass in NULL for $value or omit.

@return
  $expression, with any previous value for this option removed, and a new
  $option:$value pair added if $value was provided.
```

## Code

```php
function search_expression_insert($expression, $option, $value = NULL) {
  // Remove any previous values stored with $option.
  $expression = trim(preg_replace('/(^| )' . $option . ':[^ ]*/i', '', $expression));

  // Set new value, if provided.
  if (isset($value)) {
    $expression .= ' ' . $option . ':' . trim($value);
  }
  return $expression;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
