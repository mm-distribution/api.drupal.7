# SearchQuery::setOption()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 179–190 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L179-L190)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function setOption($option, $column)
```

## Documentation

```text
Applies a search option and removes it from the search query string.

These options are in the form option:value,value2,value3.

@param $option
  Name of the option.
@param $column
  Name of the database column to which the value should be applied.

@return
  TRUE if a value for that option was found, FALSE if not.
```

## Code

```php
  public function setOption($option, $column) {
    if ($values = search_expression_extract($this->searchExpression, $option)) {
      $or = db_or();
      foreach (explode(',', $values) as $value) {
        $or->condition($column, $value);
      }
      $this->condition($or);
      $this->searchExpression = search_expression_insert($this->searchExpression, $option);
      return TRUE;
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
