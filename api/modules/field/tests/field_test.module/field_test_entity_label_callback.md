# field_test_entity_label_callback()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 212–214 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L212-L214)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_label_callback($entity)
```

## Documentation

```text
Implements callback_entity_info_label().

@return
  The label of the entity prefixed with "label callback".
```

## Code

```php
function field_test_entity_label_callback($entity) {
  return 'label callback ' . $entity->ftlabel;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
