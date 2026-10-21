# FieldAttachOtherTestCase::testFieldAttachValidate()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1033–1117 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1033-L1117)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachValidate()
```

## Documentation

```text
Test field_attach_validate().

Verify that field_attach_validate() invokes the correct
hook_field_validate.
```

## Code

```php
  function testFieldAttachValidate() {
    $this->createFieldWithInstance('_2');

    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;

    // Set up all but one values of the first field to generate errors.
    $values = array();
    for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
      $values[$delta]['value'] = -1;
    }
    // Arrange for item 1 not to generate an error
    $values[1]['value'] = 1;
    $entity->{$this->field_name}[$langcode] = $values;

    // Set up all values of the second field to generate errors.
    $values_2 = array();
    for ($delta = 0; $delta < $this->field_2['cardinality']; $delta++) {
      $values_2[$delta]['value'] = -1;
    }
    $entity->{$this->field_name_2}[$langcode] = $values_2;

    // Validate all fields.
    try {
      field_attach_validate($entity_type, $entity);
    }
    catch (FieldValidationException $e) {
      $errors = $e->errors;
    }

    foreach ($values as $delta => $value) {
      if ($value['value'] != 1) {
        $this->assertIdentical($errors[$this->field_name][$langcode][$delta][0]['error'], 'field_test_invalid', "Error set on first field's value $delta");
        $this->assertEqual(count($errors[$this->field_name][$langcode][$delta]), 1, "Only one error set on first field's value $delta");
        unset($errors[$this->field_name][$langcode][$delta]);
      }
      else {
        $this->assertFalse(isset($errors[$this->field_name][$langcode][$delta]), "No error set on first field's value $delta");
      }
    }
    foreach ($values_2 as $delta => $value) {
      $this->assertIdentical($errors[$this->field_name_2][$langcode][$delta][0]['error'], 'field_test_invalid', "Error set on second field's value $delta");
      $this->assertEqual(count($errors[$this->field_name_2][$langcode][$delta]), 1, "Only one error set on second field's value $delta");
      unset($errors[$this->field_name_2][$langcode][$delta]);
    }
    $this->assertEqual(count($errors[$this->field_name][$langcode]), 0, 'No extraneous errors set for first field');
    $this->assertEqual(count($errors[$this->field_name_2][$langcode]), 0, 'No extraneous errors set for second field');

    // Validate a single field.
    $options = array('field_name' => $this->field_name_2);
    try {
      field_attach_validate($entity_type, $entity, $options);
    }
    catch (FieldValidationException $e) {
      $errors = $e->errors;
    }

    foreach ($values_2 as $delta => $value) {
      $this->assertIdentical($errors[$this->field_name_2][$langcode][$delta][0]['error'], 'field_test_invalid', "Error set on second field's value $delta");
      $this->assertEqual(count($errors[$this->field_name_2][$langcode][$delta]), 1, "Only one error set on second field's value $delta");
      unset($errors[$this->field_name_2][$langcode][$delta]);
    }
    $this->assertFalse(isset($errors[$this->field_name]), 'No validation errors are set for the first field, despite it having errors');
    $this->assertEqual(count($errors[$this->field_name_2][$langcode]), 0, 'No extraneous errors set for second field');

    // Check that cardinality is validated.
    $entity->{$this->field_name_2}[$langcode] = $this->_generateTestFieldValues($this->field_2['cardinality'] + 1);
    // When validating all fields.
    try {
      field_attach_validate($entity_type, $entity);
    }
    catch (FieldValidationException $e) {
      $errors = $e->errors;
    }
    $this->assertEqual($errors[$this->field_name_2][$langcode][0][0]['error'], 'field_cardinality', 'Cardinality validation failed.');
    // When validating a single field (the second field).
    try {
      field_attach_validate($entity_type, $entity, $options);
    }
    catch (FieldValidationException $e) {
      $errors = $e->errors;
    }
    $this->assertEqual($errors[$this->field_name_2][$langcode][0][0]['error'], 'field_cardinality', 'Cardinality validation failed.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
