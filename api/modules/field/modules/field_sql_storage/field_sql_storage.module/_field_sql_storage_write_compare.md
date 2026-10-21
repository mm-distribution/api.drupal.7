# _field_sql_storage_write_compare()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 505–522 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L505-L522)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_write_compare($field, $entity1, $entity2)
```

## Documentation

```text
Compare a single field value for both entities and tell us if it changed.

@param array $field
  Loaded field structure.
@param object $entity1
  First entity to compare.
@param object $entity2
  Second entity to compare.

@return bool
  True if field value changed, false otherwise.
```

## Code

```php
function _field_sql_storage_write_compare($field, $entity1, $entity2) {
  $field_name = $field['field_name'];
  if (empty($entity1->$field_name) && empty($entity2->$field_name)) {
    // Both are empty we can safely assume that it did not change.
    return FALSE;
  }
  if (!isset($entity1->$field_name) || !isset($entity2->$field_name)) {
    // One of them is missing but not the other the value changed.
    return TRUE;
  }
  // We need to proceed to deep array comparison, but we cannot do it naively:
  // in most cases the field values come from the edit form, and some Form API
  // widget values that are not field columns may be present. We need to clean
  // up both original and new field values before comparison.
  $items1 = _field_sql_storage_write_compare_filter($field, (array) $entity1->$field_name);
  $items2 = _field_sql_storage_write_compare_filter($field, (array) $entity2->$field_name);
  return $items1 != $items2;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
