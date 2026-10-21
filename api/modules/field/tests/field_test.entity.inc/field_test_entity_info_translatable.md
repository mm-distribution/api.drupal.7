# field_test_entity_info_translatable()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 146–154 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L146-L154)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_entity_info_translatable($entity_type = NULL, $translatable = NULL)
```

## Documentation

```text
Helper function to enable entity translations.
```

## Code

```php
function field_test_entity_info_translatable($entity_type = NULL, $translatable = NULL) {
  drupal_static_reset('field_has_translation_handler');
  $stored_value = &drupal_static(__FUNCTION__, array());
  if (isset($entity_type)) {
    $stored_value[$entity_type] = $translatable;
    entity_info_cache_clear();
  }
  return $stored_value;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
