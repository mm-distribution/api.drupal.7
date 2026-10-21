# search_extra_type_search_execute()

- **Type:** Function
- **File:** [`modules/search/tests/search_extra_type.module`](_file.md), lines 37–49 · [local source](../../../../../source/modules/search/tests/search_extra_type.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module#L37-L49)
- **Module/theme:** search_node_tags
- **Implements:** [hook_search_execute()](../../search.api.php/hook_search_execute.md)

## Signature

```php
function search_extra_type_search_execute($keys = NULL, $conditions = NULL)
```

## Documentation

```text
Implements hook_search_execute().

This is a dummy search, so when search "executes", we just return a dummy
result containing the keywords and a list of conditions.
```

## Code

```php
function search_extra_type_search_execute($keys = NULL, $conditions = NULL) {
  if (!$keys) {
    $keys = '';
  }
  return array(
    array(
      'link' => url('node'),
      'type' => 'Dummy result type',
      'title' => 'Dummy title',
      'snippet' => "Dummy search snippet to display. Keywords: {$keys}\n\nConditions: " . print_r($conditions, TRUE),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/search/tests/search_extra_type.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module) · Licensed GPL-2.0-or-later (see LICENSE)._
