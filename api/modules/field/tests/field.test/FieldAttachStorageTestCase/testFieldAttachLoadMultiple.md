# FieldAttachStorageTestCase::testFieldAttachLoadMultiple()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 220–291 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L220-L291)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachLoadMultiple()
```

## Documentation

```text
Test the 'multiple' load feature.
```

## Code

```php
  function testFieldAttachLoadMultiple() {
    $entity_type = 'test_entity';
    $langcode = LANGUAGE_NONE;

    // Define 2 bundles.
    $bundles = array(
      1 => 'test_bundle_1',
      2 => 'test_bundle_2',
    );
    field_test_create_bundle($bundles[1]);
    field_test_create_bundle($bundles[2]);
    // Define 3 fields:
    // - field_1 is in bundle_1 and bundle_2,
    // - field_2 is in bundle_1,
    // - field_3 is in bundle_2.
    $field_bundles_map = array(
      1 => array(1, 2),
      2 => array(1),
      3 => array(2),
    );
    for ($i = 1; $i <= 3; $i++) {
      $field_names[$i] = 'field_' . $i;
      $field = array('field_name' => $field_names[$i], 'type' => 'test_field');
      $field = field_create_field($field);
      $field_ids[$i] = $field['id'];
      foreach ($field_bundles_map[$i] as $bundle) {
        $instance = array(
          'field_name' => $field_names[$i],
          'entity_type' => 'test_entity',
          'bundle' => $bundles[$bundle],
          'settings' => array(
            // Configure the instance so that we test hook_field_load()
            // (see field_test_field_load() in field_test.module).
            'test_hook_field_load' => TRUE,
          ),
        );
        field_create_instance($instance);
      }
    }

    // Create one test entity per bundle, with random values.
    foreach ($bundles as $index => $bundle) {
      $entities[$index] = field_test_create_stub_entity($index, $index, $bundle);
      $entity = clone($entities[$index]);
      $instances = field_info_instances('test_entity', $bundle);
      foreach ($instances as $field_name => $instance) {
        $values[$index][$field_name] = mt_rand(1, 127);
        $entity->$field_name = array($langcode => array(array('value' => $values[$index][$field_name])));
      }
      field_attach_insert($entity_type, $entity);
    }

    // Check that a single load correctly loads field values for both entities.
    field_attach_load($entity_type, $entities);
    foreach ($entities as $index => $entity) {
      $instances = field_info_instances($entity_type, $bundles[$index]);
      foreach ($instances as $field_name => $instance) {
        // The field value loaded matches the one inserted.
        $this->assertEqual($entity->{$field_name}[$langcode][0]['value'], $values[$index][$field_name], format_string('Entity %index: expected value was found.', array('%index' => $index)));
        // The value added in hook_field_load() is found.
        $this->assertEqual($entity->{$field_name}[$langcode][0]['additional_key'], 'additional_value', format_string('Entity %index: extra information was found', array('%index' => $index)));
      }
    }

    // Check that the single-field load option works.
    $entity = field_test_create_stub_entity(1, 1, $bundles[1]);
    field_attach_load($entity_type, array(1 => $entity), FIELD_LOAD_CURRENT, array('field_id' => $field_ids[1]));
    $this->assertEqual($entity->{$field_names[1]}[$langcode][0]['value'], $values[1][$field_names[1]], format_string('Entity %index: expected value was found.', array('%index' => 1)));
    $this->assertEqual($entity->{$field_names[1]}[$langcode][0]['additional_key'], 'additional_value', format_string('Entity %index: extra information was found', array('%index' => 1)));
    $this->assert(!isset($entity->{$field_names[2]}), format_string('Entity %index: field %field_name is not loaded.', array('%index' => 2, '%field_name' => $field_names[2])));
    $this->assert(!isset($entity->{$field_names[3]}), format_string('Entity %index: field %field_name is not loaded.', array('%index' => 3, '%field_name' => $field_names[3])));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
