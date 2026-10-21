# ListFieldTestCase::testUpdateAllowedValues()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 52–117 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L52-L117)
- **Class:** [ListFieldTestCase](../ListFieldTestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testUpdateAllowedValues()
```

## Documentation

```text
Test that allowed values can be updated.
```

## Code

```php
  function testUpdateAllowedValues() {
    $langcode = LANGUAGE_NONE;

    // All three options appear.
    $entity = field_test_create_stub_entity();
    $form = drupal_get_form('field_test_entity_form', $entity);
    $this->assertTrue(!empty($form[$this->field_name][$langcode][1]), 'Option 1 exists');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][2]), 'Option 2 exists');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][3]), 'Option 3 exists');

    // Use one of the values in an actual entity, and check that this value
    // cannot be removed from the list.
    $entity = field_test_create_stub_entity();
    $entity->{$this->field_name}[$langcode][0] = array('value' => 1);
    field_test_entity_save($entity);
    $this->field['settings']['allowed_values'] = array(2 => 'Two');
    try {
      field_update_field($this->field);
      $this->fail(t('Cannot update a list field to not include keys with existing data.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot update a list field to not include keys with existing data.'));
    }
    // Empty the value, so that we can actually remove the option.
    $entity->{$this->field_name}[$langcode] = array();
    field_test_entity_save($entity);

    // Removed options do not appear.
    $this->field['settings']['allowed_values'] = array(2 => 'Two');
    field_update_field($this->field);
    $entity = field_test_create_stub_entity();
    $form = drupal_get_form('field_test_entity_form', $entity);
    $this->assertTrue(empty($form[$this->field_name][$langcode][1]), 'Option 1 does not exist');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][2]), 'Option 2 exists');
    $this->assertTrue(empty($form[$this->field_name][$langcode][3]), 'Option 3 does not exist');

    // Completely new options appear.
    $this->field['settings']['allowed_values'] = array(10 => 'Update', 20 => 'Twenty');
    field_update_field($this->field);
    $form = drupal_get_form('field_test_entity_form', $entity);
    $this->assertTrue(empty($form[$this->field_name][$langcode][1]), 'Option 1 does not exist');
    $this->assertTrue(empty($form[$this->field_name][$langcode][2]), 'Option 2 does not exist');
    $this->assertTrue(empty($form[$this->field_name][$langcode][3]), 'Option 3 does not exist');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][10]), 'Option 10 exists');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][20]), 'Option 20 exists');

    // Options are reset when a new field with the same name is created.
    field_delete_field($this->field_name);
    unset($this->field['id']);
    $this->field['settings']['allowed_values'] = array(1 => 'One', 2 => 'Two', 3 => 'Three');
    $this->field = field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'options_buttons',
      ),
    );
    $this->instance = field_create_instance($this->instance);
    $entity = field_test_create_stub_entity();
    $form = drupal_get_form('field_test_entity_form', $entity);
    $this->assertTrue(!empty($form[$this->field_name][$langcode][1]), 'Option 1 exists');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][2]), 'Option 2 exists');
    $this->assertTrue(!empty($form[$this->field_name][$langcode][3]), 'Option 3 exists');
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
