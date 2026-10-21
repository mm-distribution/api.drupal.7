# FieldAttachOtherTestCase::testFieldAttachForm()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1125–1160 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1125-L1160)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachForm()
```

## Documentation

```text
Test field_attach_form().

This could be much more thorough, but it does verify that the correct
widgets show up.
```

## Code

```php
  function testFieldAttachForm() {
    $this->createFieldWithInstance('_2');

    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;

    // When generating form for all fields.
    $form = array();
    $form_state = form_state_defaults();
    field_attach_form($entity_type, $entity, $form, $form_state);

    $this->assertEqual($form[$this->field_name][$langcode]['#title'], $this->instance['label'], "First field's form title is {$this->instance['label']}");
    $this->assertEqual($form[$this->field_name_2][$langcode]['#title'], $this->instance_2['label'], "Second field's form title is {$this->instance_2['label']}");
    for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
      // field_test_widget uses 'textfield'
        $this->assertEqual($form[$this->field_name][$langcode][$delta]['value']['#type'], 'textfield', "First field's form delta $delta widget is textfield");
      }
      for ($delta = 0; $delta < $this->field_2['cardinality']; $delta++) {
        // field_test_widget uses 'textfield'
        $this->assertEqual($form[$this->field_name_2][$langcode][$delta]['value']['#type'], 'textfield', "Second field's form delta $delta widget is textfield");
      }

      // When generating form for a single field (the second field).
      $options = array('field_name' => $this->field_name_2);
      $form = array();
      $form_state = form_state_defaults();
      field_attach_form($entity_type, $entity, $form, $form_state, NULL, $options);

      $this->assertFalse(isset($form[$this->field_name]), 'The first field does not exist in the form');
      $this->assertEqual($form[$this->field_name_2][$langcode]['#title'], $this->instance_2['label'], "Second field's form title is {$this->instance_2['label']}");
      for ($delta = 0; $delta < $this->field_2['cardinality']; $delta++) {
        // field_test_widget uses 'textfield'
        $this->assertEqual($form[$this->field_name_2][$langcode][$delta]['value']['#type'], 'textfield', "Second field's form delta $delta widget is textfield");
      }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
