# search_extra_type_search_page()

- **Type:** Function
- **File:** [`modules/search/tests/search_extra_type.module`](_file.md), lines 56–69 · [local source](../../../../../source/modules/search/tests/search_extra_type.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module#L56-L69)
- **Module/theme:** search_node_tags
- **Implements:** [hook_search_page()](../../search.api.php/hook_search_page.md)

## Signature

```php
function search_extra_type_search_page($results)
```

## Documentation

```text
Implements hook_search_page().

Adds some text to the search page so we can verify that it runs.
```

## Code

```php
function search_extra_type_search_page($results) {
  $output['prefix']['#markup'] = '<h2>Test page text is here</h2> <ol class="search-results">';

  foreach ($results as $entry) {
    $output[] = array(
      '#theme' => 'search_result',
      '#result' => $entry,
      '#module' => 'search_extra_type',
    );
  }
  $output['suffix']['#markup'] = '</ol>' . theme('pager');

  return $output;
}
```

---
_Drupal 7.103 · [modules/search/tests/search_extra_type.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module) · Licensed GPL-2.0-or-later (see LICENSE)._
