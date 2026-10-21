# FieldCrudTestCase::testReadFields()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2563–2593 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2563-L2593)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testReadFields()
```

## Documentation

```text
Tests reading field definitions.
```

## Code

```php
  function testReadFields() {
    $field_definition = array(
      'field_name' => 'field_1',
      'type' => 'test_field',
    );
    field_create_field($field_definition);

    // Check that 'single column' criteria works.
    $fields = field_read_fields(array('field_name' => $field_definition['field_name']));
    $this->assertTrue(count($fields) == 1 && isset($fields[$field_definition['field_name']]), 'The field was properly read.');

    // Check that 'multi column' criteria works.
    $fields = field_read_fields(array('field_name' => $field_definition['field_name'], 'type' => $field_definition['type']));
    $this->assertTrue(count($fields) == 1 && isset($fields[$field_definition['field_name']]), 'The field was properly read.');
    $fields = field_read_fields(array('field_name' => $field_definition['field_name'], 'type' => 'foo'));
    $this->assertTrue(empty($fields), 'No field was found.');

    // Create an instance of the field.
    $instance_definition = array(
      'field_name' => $field_definition['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
    );
    field_create_instance($instance_definition);

    // Check that criteria spanning over the field_config_instance table work.
    $fields = field_read_fields(array('entity_type' => $instance_definition['entity_type'], 'bundle' => $instance_definition['bundle']));
    $this->assertTrue(count($fields) == 1 && isset($fields[$field_definition['field_name']]), 'The field was properly read.');
    $fields = field_read_fields(array('entity_type' => $instance_definition['entity_type'], 'field_name' => $instance_definition['field_name']));
    $this->assertTrue(count($fields) == 1 && isset($fields[$field_definition['field_name']]), 'The field was properly read.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
