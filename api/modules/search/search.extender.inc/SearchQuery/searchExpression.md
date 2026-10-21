# SearchQuery::searchExpression()

- **Type:** Method
- **File:** [`modules/search/search.extender.inc`](../_file.md), lines 148–164 · [local source](../../../../../source/modules/search/search.extender.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc#L148-L164)
- **Class:** [SearchQuery](../SearchQuery.md)
- **Module/theme:** search

## Signature

```php
public function searchExpression($expression, $module)
```

## Documentation

```text
Sets up the search query expression.

@param $query
  A search query string, which can contain options.
@param $module
  The search module. This maps to {search_index}.type in the database.

@return
  The SearchQuery object.
```

## Code

```php
  public function searchExpression($expression, $module) {
    $this->searchExpression = $expression;
    $this->type = $module;

    // Add a search_* tag. This needs to be added before any preExecute methods
    // for decorated queries are called, as $this->prepared will be set to TRUE
    // and tags added in the execute method will never get used. For example,
    // if $query is extended by 'SearchQuery' then 'PagerDefault', the
    // search-specific tag will be added too late (when preExecute() has
    // already been called from the PagerDefault extender), and as a
    // consequence will not be available to hook_query_alter() implementations,
    // nor will the correct hook_query_TAG_alter() implementations get invoked.
    // See node_search_execute().
    $this->addTag('search_' . $module);

    return $this;
  }
```

---
_Drupal 7.103 · [modules/search/search.extender.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.extender.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
