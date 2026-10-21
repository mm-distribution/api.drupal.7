# FieldCrudTestCase::testUpdateField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2747–2787 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2747-L2787)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testUpdateField()
```

## Documentation

```text
Test updating a field.
```

## Code

```php
  function testUpdateField() {
    // Create a field with a defined cardinality, so that we can ensure it's
    // respected. Since cardinality enforcement is consistent across database
    // systems, it makes a good test case.
    $cardinality = 4;
    $field_definition = array(
      'field_name' => 'field_update',
      'type' => 'test_field',
      'cardinality' => $cardinality,
    );
    $field_definition = field_create_field($field_definition);
    $instance = array(
      'field_name' => 'field_update',
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
    );
    $instance = field_create_instance($instance);

    do {
      // We need a unique ID for our entity. $cardinality will do.
      $id = $cardinality;
      $entity = field_test_create_stub_entity($id, $id, $instance['bundle']);
      // Fill in the entity with more values than $cardinality.
      for ($i = 0; $i < 20; $i++) {
        $entity->field_update[LANGUAGE_NONE][$i]['value'] = $i;
      }
      // Save the entity.
      field_attach_insert('test_entity', $entity);
      // Load back and assert there are $cardinality number of values.
      $entity = field_test_create_stub_entity($id, $id, $instance['bundle']);
      field_attach_load('test_entity', array($id => $entity));
      $this->assertEqual(count($entity->field_update[LANGUAGE_NONE]), $field_definition['cardinality'], 'Cardinality is kept');
      // Now check the values themselves.
      for ($delta = 0; $delta < $cardinality; $delta++) {
        $this->assertEqual($entity->field_update[LANGUAGE_NONE][$delta]['value'], $delta, 'Value is kept');
      }
      // Increase $cardinality and set the field cardinality to the new value.
      $field_definition['cardinality'] = ++$cardinality;
      field_update_field($field_definition);
    } while ($cardinality < 6);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
