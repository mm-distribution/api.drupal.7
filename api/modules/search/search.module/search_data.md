# search_data()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1098–1112 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1098-L1112)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function search_data($keys, $module, $conditions = NULL)
```

## Documentation

```text
Performs a search by calling hook_search_execute().

@param $keys
  Keyword query to search on.
@param $module
  Search module to search.
@param $conditions
  Optional array of additional search conditions.

@return
  Renderable array of search results. No return value if $keys are not
  supplied or if the given search module is not active.
```

## Code

```php
function search_data($keys, $module, $conditions = NULL) {
  if (module_hook($module, 'search_execute')) {
    $results = module_invoke($module, 'search_execute', $keys, $conditions);
    if (module_hook($module, 'search_page')) {
      return module_invoke($module, 'search_page', $results);
    }
    else {
      return array(
        '#theme' => 'search_results',
        '#results' => $results,
        '#module' => $module,
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
