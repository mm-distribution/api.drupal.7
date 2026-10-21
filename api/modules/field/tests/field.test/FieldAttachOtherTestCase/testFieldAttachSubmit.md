# FieldAttachOtherTestCase::testFieldAttachSubmit()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1165–1245 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1165-L1245)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachSubmit()
```

## Documentation

```text
Test field_attach_submit().
```

## Code

```php
  function testFieldAttachSubmit() {
    $this->createFieldWithInstance('_2');

    $entity_type = 'test_entity';
    $entity_init = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;

    // Build the form for all fields.
    $form = array();
    $form_state = form_state_defaults();
    field_attach_form($entity_type, $entity_init, $form, $form_state);

    // Simulate incoming values.
    // First field.
    $values = array();
    $weights = array();
    for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
      $values[$delta]['value'] = mt_rand(1, 127);
      // Assign random weight.
      do {
        $weight = mt_rand(0, $this->field['cardinality']);
      } while (in_array($weight, $weights));
      $weights[$delta] = $weight;
      $values[$delta]['_weight'] = $weight;
    }
    // Leave an empty value. 'field_test' fields are empty if empty().
    $values[1]['value'] = 0;
    // Second field.
    $values_2 = array();
    $weights_2 = array();
    for ($delta = 0; $delta < $this->field_2['cardinality']; $delta++) {
      $values_2[$delta]['value'] = mt_rand(1, 127);
      // Assign random weight.
      do {
        $weight = mt_rand(0, $this->field_2['cardinality']);
      } while (in_array($weight, $weights_2));
      $weights_2[$delta] = $weight;
      $values_2[$delta]['_weight'] = $weight;
    }
    // Leave an empty value. 'field_test' fields are empty if empty().
    $values_2[1]['value'] = 0;
    // Pretend the form has been built.
    drupal_prepare_form('field_test_entity_form', $form, $form_state);
    drupal_process_form('field_test_entity_form', $form, $form_state);
    $form_state['values'][$this->field_name][$langcode] = $values;
    $form_state['values'][$this->field_name_2][$langcode] = $values_2;

    // Call field_attach_submit() for all fields.
    $entity = clone($entity_init);
    field_attach_submit($entity_type, $entity, $form, $form_state);

    asort($weights);
    asort($weights_2);
    $expected_values = array();
    $expected_values_2 = array();
    foreach ($weights as $key => $value) {
      if ($key != 1) {
        $expected_values[] = array('value' => $values[$key]['value']);
      }
    }
    $this->assertIdentical($entity->{$this->field_name}[$langcode], $expected_values, 'Submit filters empty values');
    foreach ($weights_2 as $key => $value) {
      if ($key != 1) {
        $expected_values_2[] = array('value' => $values_2[$key]['value']);
      }
    }
    $this->assertIdentical($entity->{$this->field_name_2}[$langcode], $expected_values_2, 'Submit filters empty values');

    // Call field_attach_submit() for a single field (the second field).
    $options = array('field_name' => $this->field_name_2);
    $entity = clone($entity_init);
    field_attach_submit($entity_type, $entity, $form, $form_state, $options);
    $expected_values_2 = array();
    foreach ($weights_2 as $key => $value) {
      if ($key != 1) {
        $expected_values_2[] = array('value' => $values_2[$key]['value']);
      }
    }
    $this->assertFalse(isset($entity->{$this->field_name}), 'The first field does not exist in the entity object');
    $this->assertIdentical($entity->{$this->field_name_2}[$langcode], $expected_values_2, 'Submit filters empty values');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
