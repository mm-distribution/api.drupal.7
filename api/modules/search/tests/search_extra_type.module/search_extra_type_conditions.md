# search_extra_type_conditions()

- **Type:** Function
- **File:** [`modules/search/tests/search_extra_type.module`](_file.md), lines 22–29 · [local source](../../../../../source/modules/search/tests/search_extra_type.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module#L22-L29)
- **Module/theme:** search_node_tags

## Signature

```php
function search_extra_type_conditions()
```

## Documentation

```text
Test conditions callback for hook_search_info().
```

## Code

```php
function search_extra_type_conditions() {
  $conditions = array();

  if (!empty($_REQUEST['search_conditions'])) {
    $conditions['search_conditions'] = $_REQUEST['search_conditions'];
  }
  return $conditions;
}
```

---
_Drupal 7.103 · [modules/search/tests/search_extra_type.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_extra_type.module) · Licensed GPL-2.0-or-later (see LICENSE)._
