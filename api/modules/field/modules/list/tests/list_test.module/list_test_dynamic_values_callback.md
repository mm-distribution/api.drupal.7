# list_test_dynamic_values_callback()

- **Type:** Function
- **File:** [`modules/field/modules/list/tests/list_test.module`](_file.md), lines 28–32 · [local source](../../../../../../../source/modules/field/modules/list/tests/list_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list_test.module#L28-L32)
- **Module/theme:** list_test

## Signature

```php
function list_test_dynamic_values_callback($field, $instance, $entity_type, $entity, &$cacheable)
```

## Documentation

```text
An entity-bound allowed values callback.
```

## Code

```php
function list_test_dynamic_values_callback($field, $instance, $entity_type, $entity, &$cacheable) {
  $cacheable = FALSE;
  // We need the values of the entity as keys.
  return drupal_map_assoc(array_merge(array($entity->ftlabel), entity_extract_ids($entity_type, $entity)));
}
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
