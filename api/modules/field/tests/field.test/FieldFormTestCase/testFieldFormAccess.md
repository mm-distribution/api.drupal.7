# FieldFormTestCase::testFieldFormAccess()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1994–2060 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1994-L2060)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormAccess()
```

## Documentation

```text
Tests fields with no 'edit' access.
```

## Code

```php
  function testFieldFormAccess() {
    // Create a "regular" field.
    $field = $this->field_single;
    $field_name = $field['field_name'];
    $instance = $this->instance;
    $instance['field_name'] = $field_name;
    field_create_field($field);
    field_create_instance($instance);

    // Create a field with no edit access - see field_test_field_access().
    $field_no_access = array(
      'field_name' => 'field_no_edit_access',
      'type' => 'test_field',
    );
    $field_name_no_access = $field_no_access['field_name'];
    $instance_no_access = array(
      'field_name' => $field_name_no_access,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'default_value' => array(0 => array('value' => 99)),
    );
    field_create_field($field_no_access);
    field_create_instance($instance_no_access);

    $langcode = LANGUAGE_NONE;

    // Test that the form structure includes full information for each delta
    // apart from #access.
    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);

    $form = array();
    $form_state = form_state_defaults();
    field_attach_form($entity_type, $entity, $form, $form_state);

    $this->assertEqual($form[$field_name_no_access][$langcode][0]['value']['#entity_type'], $entity_type, 'The correct entity type is set in the field structure.');
    $this->assertFalse($form[$field_name_no_access]['#access'], 'Field #access is FALSE for the field without edit access.');

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertNoFieldByName("{$field_name_no_access}[$langcode][0][value]", '', 'Widget is not displayed if field access is denied.');

    // Create entity.
    $edit = array("{$field_name}[$langcode][0][value]" => 1);
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];

    // Check that the default value was saved.
    $entity = field_test_entity_test_load($id);
    $this->assertEqual($entity->{$field_name_no_access}[$langcode][0]['value'], 99, 'Default value was saved for the field with no edit access.');
    $this->assertEqual($entity->{$field_name}[$langcode][0]['value'], 1, 'Entered value vas saved for the field with edit access.');

    // Create a new revision.
    $edit = array("{$field_name}[$langcode][0][value]" => 2, 'revision' => TRUE);
    $this->drupalPost('test-entity/manage/' . $id . '/edit', $edit, t('Save'));

    // Check that the new revision has the expected values.
    $entity = field_test_entity_test_load($id);
    $this->assertEqual($entity->{$field_name_no_access}[$langcode][0]['value'], 99, 'New revision has the expected value for the field with no edit access.');
    $this->assertEqual($entity->{$field_name}[$langcode][0]['value'], 2, 'New revision has the expected value for the field with edit access.');

    // Check that the revision is also saved in the revisions table.
    $entity = field_test_entity_test_load($id, $entity->ftvid);
    $this->assertEqual($entity->{$field_name_no_access}[$langcode][0]['value'], 99, 'New revision has the expected value for the field with no edit access.');
    $this->assertEqual($entity->{$field_name}[$langcode][0]['value'], 2, 'New revision has the expected value for the field with edit access.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
