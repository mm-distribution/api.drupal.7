# FieldAttachStorageTestCase::testFieldStorageDetailsAlter()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 349–384 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L349-L384)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldStorageDetailsAlter()
```

## Documentation

```text
Test storage details alteration.

@see field_test_storage_details_alter()
```

## Code

```php
  function testFieldStorageDetailsAlter() {
    $field_name = 'field_test_change_my_details';
    $field = array(
      'field_name' => $field_name,
      'type' => 'test_field',
      'cardinality' => 4,
      'storage' => array('type' => 'field_test_storage'),
    );
    $field = field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
    );
    field_create_instance($instance);

    $field = field_info_field($instance['field_name']);
    $instance = field_info_instance($instance['entity_type'], $instance['field_name'], $instance['bundle']);

    // The storage details are indexed by a storage engine type.
    $this->assertTrue(array_key_exists('drupal_variables', $field['storage']['details']), 'The storage type is Drupal variables.');

    $details = $field['storage']['details']['drupal_variables'];

    // The field_test storage details are indexed by variable name. The details
    // are altered, so moon and mars are correct for this test.
    $this->assertTrue(array_key_exists('moon', $details[FIELD_LOAD_CURRENT]), 'Moon is available in the instance array.');
    $this->assertTrue(array_key_exists('mars', $details[FIELD_LOAD_REVISION]), 'Mars is available in the instance array.');

    // Test current and revision storage details together because the columns
    // are the same.
    foreach ((array) $field['columns'] as $column_name => $attributes) {
      $this->assertEqual($details[FIELD_LOAD_CURRENT]['moon'][$column_name], $column_name, format_string('Column name %value matches the definition in %bin.', array('%value' => $column_name, '%bin' => 'moon[FIELD_LOAD_CURRENT]')));
      $this->assertEqual($details[FIELD_LOAD_REVISION]['mars'][$column_name], $column_name, format_string('Column name %value matches the definition in %bin.', array('%value' => $column_name, '%bin' => 'mars[FIELD_LOAD_REVISION]')));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
