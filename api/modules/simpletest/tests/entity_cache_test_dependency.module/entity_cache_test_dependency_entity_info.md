# entity_cache_test_dependency_entity_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_cache_test_dependency.module`](_file.md), lines 11–17 · [local source](../../../../../source/modules/simpletest/tests/entity_cache_test_dependency.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_cache_test_dependency.module#L11-L17)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_info()](../../../system/system.api.php/hook_entity_info.md)

## Signature

```php
function entity_cache_test_dependency_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function entity_cache_test_dependency_entity_info() {
  return array(
    'entity_cache_test' => array(
      'label' => variable_get('entity_cache_test_label', 'Entity Cache Test'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_cache_test_dependency.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_cache_test_dependency.module) · Licensed GPL-2.0-or-later (see LICENSE)._
