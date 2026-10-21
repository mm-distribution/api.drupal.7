# field_test_field_test_op_multiple()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 88–99 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L88-L99)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_field_test_op_multiple($entity_type, $entities, $field, $instances, $langcode, &$items)
```

## Documentation

```text
Generic op to test _field_invoke_multiple behavior.

This simulates a multiple field operation callback to be invoked by
_field_invoke_multiple().
```

## Code

```php
function field_test_field_test_op_multiple($entity_type, $entities, $field, $instances, $langcode, &$items) {
  $result = array();
  foreach ($entities as $id => $entity) {
    // Entities, instances and items are assumed to be consistently grouped by
    // language. To verify this we try to access all the passed data structures
    // by entity id. If they are grouped correctly, one entity, one instance and
    // one array of items should be available for each entity id.
    $field_name = $instances[$id]['field_name'];
    $result[$id] = array($langcode => hash('sha256', serialize(array($entity_type, $entity, $field_name, $langcode, $items[$id]))));
  }
  return $result;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
