# hook_search_page()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 248–261 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L248-L261)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_search_page($results)
```

## Documentation

```text
Override the rendering of search results.

A module that implements hook_search_info() to define a type of search may
implement this hook in order to override the default theming of its search
results, which is otherwise themed using theme('search_results').

Note that by default, theme('search_results') and theme('search_result')
work together to create an ordered list (OL). So your hook_search_page()
implementation should probably do this as well.

@param $results
  An array of search results.

@return
  A renderable array, which will render the formatted search results with a
  pager included.

@see search-result.tpl.php
@see search-results.tpl.php
```

## Code

```php
function hook_search_page($results) {
  $output['prefix']['#markup'] = '<ol class="search-results">';

  foreach ($results as $entry) {
    $output[] = array(
      '#theme' => 'search_result',
      '#result' => $entry,
      '#module' => 'my_module_name',
    );
  }
  $output['suffix']['#markup'] = '</ol>' . theme('pager');

  return $output;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_page()".

- [search_extra_type_search_page()](../tests/search_extra_type.module/search_extra_type_search_page.md) — `modules/search/tests/search_extra_type.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
