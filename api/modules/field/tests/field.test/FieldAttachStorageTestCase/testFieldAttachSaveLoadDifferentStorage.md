# FieldAttachStorageTestCase::testFieldAttachSaveLoadDifferentStorage()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 296–342 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L296-L342)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachSaveLoadDifferentStorage()
```

## Documentation

```text
Test saving and loading fields using different storage backends.
```

## Code

```php
  function testFieldAttachSaveLoadDifferentStorage() {
    $entity_type = 'test_entity';
    $langcode = LANGUAGE_NONE;

    // Create two fields using different storage backends, and their instances.
    $fields = array(
      array(
        'field_name' => 'field_1',
        'type' => 'test_field',
        'cardinality' => 4,
        'storage' => array('type' => 'field_sql_storage')
      ),
      array(
        'field_name' => 'field_2',
        'type' => 'test_field',
        'cardinality' => 4,
        'storage' => array('type' => 'field_test_storage')
      ),
    );
    foreach ($fields as $field) {
      field_create_field($field);
      $instance = array(
        'field_name' => $field['field_name'],
        'entity_type' => 'test_entity',
        'bundle' => 'test_bundle',
      );
      field_create_instance($instance);
    }

    $entity_init = field_test_create_stub_entity();

    // Create entity and insert random values.
    $entity = clone($entity_init);
    $values = array();
    foreach ($fields as $field) {
      $values[$field['field_name']] = $this->_generateTestFieldValues($this->field['cardinality']);
      $entity->{$field['field_name']}[$langcode] = $values[$field['field_name']];
    }
    field_attach_insert($entity_type, $entity);

    // Check that values are loaded as expected.
    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    foreach ($fields as $field) {
      $this->assertEqual($values[$field['field_name']], $entity->{$field['field_name']}[$langcode], format_string('%storage storage: expected values were found.', array('%storage' => $field['storage']['type'])));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
