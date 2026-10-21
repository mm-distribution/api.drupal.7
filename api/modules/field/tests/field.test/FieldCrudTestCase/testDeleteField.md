# FieldCrudTestCase::testDeleteField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2641–2717 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2641-L2717)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testDeleteField()
```

## Documentation

```text
Test the deletion of a field.
```

## Code

```php
  function testDeleteField() {
    // TODO: Also test deletion of the data stored in the field ?

    // Create two fields (so we can test that only one is deleted).
    $this->field = array('field_name' => 'field_1', 'type' => 'test_field');
    field_create_field($this->field);
    $this->another_field = array('field_name' => 'field_2', 'type' => 'test_field');
    field_create_field($this->another_field);

    // Create instances for each.
    $this->instance_definition = array(
      'field_name' => $this->field['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'test_field_widget',
      ),
    );
    field_create_instance($this->instance_definition);
    $this->another_instance_definition = $this->instance_definition;
    $this->another_instance_definition['field_name'] = $this->another_field['field_name'];
    field_create_instance($this->another_instance_definition);

    // Test that the first field is not deleted, and then delete it.
    $field = field_read_field($this->field['field_name'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($field) && empty($field['deleted']), 'A new field is not marked for deletion.');
    field_delete_field($this->field['field_name']);

    // Make sure that the field is marked as deleted when it is specifically
    // loaded.
    $field = field_read_field($this->field['field_name'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($field['deleted']), 'A deleted field is marked for deletion.');

    // Make sure that this field's instance is marked as deleted when it is
    // specifically loaded.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($instance['deleted']), 'An instance for a deleted field is marked for deletion.');

    // Try to load the field normally and make sure it does not show up.
    $field = field_read_field($this->field['field_name']);
    $this->assertTrue(empty($field), 'A deleted field is not loaded by default.');

    // Try to load the instance normally and make sure it does not show up.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertTrue(empty($instance), 'An instance for a deleted field is not loaded by default.');

    // Make sure the other field (and its field instance) are not deleted.
    $another_field = field_read_field($this->another_field['field_name']);
    $this->assertTrue(!empty($another_field) && empty($another_field['deleted']), 'A non-deleted field is not marked for deletion.');
    $another_instance = field_read_instance('test_entity', $this->another_instance_definition['field_name'], $this->another_instance_definition['bundle']);
    $this->assertTrue(!empty($another_instance) && empty($another_instance['deleted']), 'An instance of a non-deleted field is not marked for deletion.');

    // Try to create a new field the same name as a deleted field and
    // write data into it.
    field_create_field($this->field);
    field_create_instance($this->instance_definition);
    $field = field_read_field($this->field['field_name']);
    $this->assertTrue(!empty($field) && empty($field['deleted']), 'A new field with a previously used name is created.');
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertTrue(!empty($instance) && empty($instance['deleted']), 'A new instance for a previously used field name is created.');

    // Save an entity with data for the field
    $entity = field_test_create_stub_entity(0, 0, $instance['bundle']);
    $langcode = LANGUAGE_NONE;
    $values[0]['value'] = mt_rand(1, 127);
    $entity->{$field['field_name']}[$langcode] = $values;
    $entity_type = 'test_entity';
    field_attach_insert('test_entity', $entity);

    // Verify the field is present on load
    $entity = field_test_create_stub_entity(0, 0, $this->instance_definition['bundle']);
    field_attach_load($entity_type, array(0 => $entity));
    $this->assertIdentical(count($entity->{$field['field_name']}[$langcode]), count($values), "Data in previously deleted field saves and loads correctly");
    foreach ($values as $delta => $value) {
      $this->assertEqual($entity->{$field['field_name']}[$langcode][$delta]['value'], $values[$delta]['value'], "Data in previously deleted field saves and loads correctly");
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
