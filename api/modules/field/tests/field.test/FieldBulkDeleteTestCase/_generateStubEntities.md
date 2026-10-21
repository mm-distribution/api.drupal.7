# FieldBulkDeleteTestCase::_generateStubEntities()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3541–3551 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3541-L3551)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function _generateStubEntities($entity_type, $entities, $field_name = NULL)
```

## Documentation

```text
Convenience function for Field API tests.

Given an array of potentially fully-populated entities and an
optional field name, generate an array of stub entities of the
same fieldable type which contains the data for the field name
(if given).

@param $entity_type
  The entity type of $entities.
@param $entities
  An array of entities of type $entity_type.
@param $field_name
  Optional; a field name whose data should be copied from
  $entities into the returned stub entities.
@return
  An array of stub entities corresponding to $entities.
```

## Code

```php
  function _generateStubEntities($entity_type, $entities, $field_name = NULL) {
    $stubs = array();
    foreach ($entities as $id => $entity) {
      $stub = entity_create_stub_entity($entity_type, entity_extract_ids($entity_type, $entity));
      if (isset($field_name)) {
        $stub->{$field_name} = $entity->{$field_name};
      }
      $stubs[$id] = $stub;
    }
    return $stubs;
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
