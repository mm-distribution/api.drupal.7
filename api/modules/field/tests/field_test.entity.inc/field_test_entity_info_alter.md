# field_test_entity_info_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 132–141 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L132-L141)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_entity_info_alter()](../../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function field_test_entity_info_alter(&$entity_info)
```

## Documentation

```text
Implements hook_entity_info_alter().
```

## Code

```php
function field_test_entity_info_alter(&$entity_info) {
  // Enable/disable field_test as a translation handler.
  foreach (field_test_entity_info_translatable() as $entity_type => $translatable) {
    $entity_info[$entity_type]['translation']['field_test'] = $translatable;
  }
  // Disable locale as a translation handler.
  foreach ($entity_info as $entity_type => $info) {
    $entity_info[$entity_type]['translation']['locale'] = FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
