# FieldSqlStorageTestCase::testUpdateFieldSchemaWithData()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 379–398 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L379-L398)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testUpdateFieldSchemaWithData()
```

## Documentation

```text
Test trying to update a field with data.
```

## Code

```php
  function testUpdateFieldSchemaWithData() {
    // Create a decimal 5.2 field and add some data.
    $field = array('field_name' => 'decimal52', 'type' => 'number_decimal', 'settings' => array('precision' => 5, 'scale' => 2));
    $field = field_create_field($field);
    $instance = array('field_name' => 'decimal52', 'entity_type' => 'test_entity', 'bundle' => 'test_bundle');
    $instance = field_create_instance($instance);
    $entity = field_test_create_stub_entity(0, 0, $instance['bundle']);
    $entity->decimal52[LANGUAGE_NONE][0]['value'] = '1.235';
    field_attach_insert('test_entity', $entity);

    // Attempt to update the field in a way that would work without data.
    $field['settings']['scale'] = 3;
    try {
      field_update_field($field);
      $this->fail(t('Cannot update field schema with data.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot update field schema with data.'));
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
