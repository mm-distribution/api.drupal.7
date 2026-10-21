# callback_search_conditions()

- **Type:** Function
- **File:** [`modules/search/search.api.php`](_file.md), lines 367–380 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L367-L380)
- **Module/theme:** search
- **Topics:** [callbacks](../../../topics/callbacks.md), [search](../../../topics/search.md)

## Signature

```php
function callback_search_conditions($keys)
```

## Documentation

```text
Provide search query conditions.

Callback for hook_search_info().

This callback is invoked by search_view() to get an array of additional
search conditions to pass to search_data(). For example, a search module
may get additional keywords, filters, or modifiers for the search from
the query string.

This example pulls additional search keywords out of the $_REQUEST variable,
(i.e. from the query string of the request). The conditions may also be
generated internally - for example based on a module's settings.

@param $keys
  The search keywords string.

@return
  An array of additional conditions, such as filters.

@ingroup callbacks
@ingroup search
```

## Code

```php
function callback_search_conditions($keys) {
  $conditions = array();

  if (!empty($_REQUEST['keys'])) {
    $conditions['keys'] = $_REQUEST['keys'];
  }
  if (!empty($_REQUEST['sample_search_keys'])) {
    $conditions['sample_search_keys'] = $_REQUEST['sample_search_keys'];
  }
  if ($force_keys = config('sample_search.settings')->get('force_keywords')) {
    $conditions['sample_search_force_keywords'] = $force_keys;
  }
  return $conditions;
}
```

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
