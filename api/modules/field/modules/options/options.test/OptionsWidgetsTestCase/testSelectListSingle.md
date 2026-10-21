# OptionsWidgetsTestCase::testSelectListSingle()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 226–324 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L226-L324)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function testSelectListSingle()
```

## Documentation

```text
Tests the 'options_select' widget (single select).
```

## Code

```php
  function testSelectListSingle() {
    // Create an instance of the 'single value' field.
    $instance = array(
      'field_name' => $this->card_1['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'required' => TRUE,
      'widget' => array(
        'type' => 'options_select',
      ),
    );
    $instance = field_create_instance($instance);
    $langcode = LANGUAGE_NONE;

    // Create an entity.
    $entity_init = field_test_create_stub_entity();
    $entity = clone $entity_init;
    $entity->is_new = TRUE;
    field_test_entity_save($entity);

    // Display form.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    // A required field without any value has a "none" option.
    $this->assertTrue($this->xpath('//select[@id=:id]//option[@value="_none" and text()=:label]', array(':id' => 'edit-card-1-' . $langcode, ':label' => t('- Select a value -'))), 'A required select list has a "Select a value" choice.');

    // With no field data, nothing is selected.
    $this->assertNoOptionSelected("edit-card-1-$langcode", '_none');
    $this->assertNoOptionSelected("edit-card-1-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 2);
    $this->assertRaw('Some dangerous &amp; unescaped markup', 'Option text was properly filtered.');
    $this->assertRaw('Some HTML encoded markup with &lt; &amp; &gt;', 'HTML entities in option text were properly handled and not double-encoded');

    // Submit form: select invalid 'none' option.
    $edit = array("card_1[$langcode]" => '_none');
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('!title field is required.', array('!title' => $instance['field_name'])), 'Cannot save a required field when selecting "none" from the select list.');

    // Submit form: select first option.
    $edit = array("card_1[$langcode]" => 0);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    // A required field with a value has no 'none' option.
    $this->assertFalse($this->xpath('//select[@id=:id]//option[@value="_none"]', array(':id' => 'edit-card-1-' . $langcode)), 'A required select list with an actual value has no "none" choice.');
    $this->assertOptionSelected("edit-card-1-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 2);

    // Make the field non required.
    $instance['required'] = FALSE;
    field_update_instance($instance);

    // Display form.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    // A non-required field has a 'none' option.
    $this->assertTrue($this->xpath('//select[@id=:id]//option[@value="_none" and text()=:label]', array(':id' => 'edit-card-1-' . $langcode, ':label' => t('- None -'))), 'A non-required select list has a "None" choice.');
    // Submit form: Unselect the option.
    $edit = array("card_1[$langcode]" => '_none');
    $this->drupalPost('test-entity/manage/' . $entity->ftid . '/edit', $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array());

    // Test optgroups.

    $this->card_1['settings']['allowed_values'] = array();
    $this->card_1['settings']['allowed_values_function'] = 'list_test_allowed_values_callback';
    field_update_field($this->card_1);

    // Display form: with no field data, nothing is selected
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoOptionSelected("edit-card-1-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 2);
    $this->assertRaw('Some dangerous &amp; unescaped markup', 'Option text was properly filtered.');
    $this->assertRaw('Group 1', 'Option groups are displayed.');

    // Submit form: select first option.
    $edit = array("card_1[$langcode]" => 0);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertOptionSelected("edit-card-1-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-1-$langcode", 2);

    // Submit form: Unselect the option.
    $edit = array("card_1[$langcode]" => '_none');
    $this->drupalPost('test-entity/manage/' . $entity->ftid . '/edit', $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array());

    // Submit form: select the option from optgroup.
    $edit = array("card_1[$langcode]" => 2);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array(2));
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
