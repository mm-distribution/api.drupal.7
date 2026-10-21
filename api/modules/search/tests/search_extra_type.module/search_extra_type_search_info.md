# search_extra_type_search_info()

- **Type:** Function
- **File:** [`modules/search/tests/search_extra_type.module`](_file.md), lines 11–17 · [local source](../../../../../source/modules/search/tests/search_extra_type.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module#L11-L17)
- **Module/theme:** search_node_tags
- **Implements:** [hook_search_info()](../../search.api.php/hook_search_info.md)

## Signature

```php
function search_extra_type_search_info()
```

## Documentation

```text
Implements hook_search_info().
```

## Code

```php
function search_extra_type_search_info() {
  return array(
    'title' => 'Dummy search type',
    'path' => 'dummy_path',
    'conditions_callback' => 'search_extra_type_conditions',
  );
}
```

---
_Drupal 7.103 · [modules/search/tests/search_extra_type.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module) · Licensed GPL-2.0-or-later (see LICENSE)._
