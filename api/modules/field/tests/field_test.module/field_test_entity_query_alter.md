# field_test_entity_query_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 188–192 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L188-L192)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_entity_query_alter()](../../../system/system.api.php/hook_entity_query_alter.md)

## Signature

```php
function field_test_entity_query_alter(&$query)
```

## Documentation

```text
Implements hook_entity_query_alter().
```

## Code

```php
function field_test_entity_query_alter(&$query) {
  if (variable_get('field_test_entity_query_alter_execute_callback', FALSE)) {
    $query->executeCallback = 'field_test_dummy_field_storage_query';
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
