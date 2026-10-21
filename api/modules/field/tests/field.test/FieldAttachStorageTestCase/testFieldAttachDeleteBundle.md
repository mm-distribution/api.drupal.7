# FieldAttachStorageTestCase::testFieldAttachDeleteBundle()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 655–710 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L655-L710)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachDeleteBundle()
```

## Documentation

```text
Test field_attach_delete_bundle().
```

## Code

```php
  function testFieldAttachDeleteBundle() {
    // Create a new bundle. This has to be initiated by the module so that its
    // hook_entity_info() is consistent.
    $new_bundle = 'test_bundle_' . drupal_strtolower($this->randomName());
    field_test_create_bundle($new_bundle);

    // Add an instance to that bundle.
    $this->instance['bundle'] = $new_bundle;
    field_create_instance($this->instance);

    // Create a second field for the test bundle
    $field_name = drupal_strtolower($this->randomName() . '_field_name');
    $field = array('field_name' => $field_name, 'type' => 'test_field', 'cardinality' => 1);
    field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'test_entity',
      'bundle' => $this->instance['bundle'],
      'label' => $this->randomName() . '_label',
      'description' => $this->randomName() . '_description',
      'weight' => mt_rand(0, 127),
      // test_field has no instance settings
      'widget' => array(
        'type' => 'test_field_widget',
        'settings' => array(
          'size' => mt_rand(0, 255))));
    field_create_instance($instance);

    // Save an entity with data for both fields
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity->{$this->field_name}[$langcode] = $values;
    $entity->{$field_name}[$langcode] = $this->_generateTestFieldValues(1);
    field_attach_insert('test_entity', $entity);

    // Verify the fields are present on load
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    field_attach_load('test_entity', array(0 => $entity));
    $this->assertEqual(count($entity->{$this->field_name}[$langcode]), 4, 'First field got loaded');
    $this->assertEqual(count($entity->{$field_name}[$langcode]), 1, 'Second field got loaded');

    // Delete the bundle. This has to be initiated by the module so that its
    // hook_entity_info() is consistent.
    field_test_delete_bundle($this->instance['bundle']);

    // Verify no data gets loaded
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    field_attach_load('test_entity', array(0 => $entity));
    $this->assertFalse(isset($entity->{$this->field_name}[$langcode]), 'No data for first field');
    $this->assertFalse(isset($entity->{$field_name}[$langcode]), 'No data for second field');

    // Verify that the instances are gone
    $this->assertFalse(field_read_instance('test_entity', $this->field_name, $this->instance['bundle']), "First field is deleted");
    $this->assertFalse(field_read_instance('test_entity', $field_name, $instance['bundle']), "Second field is deleted");
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
