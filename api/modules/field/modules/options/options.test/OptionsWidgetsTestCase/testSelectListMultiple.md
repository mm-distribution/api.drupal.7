# OptionsWidgetsTestCase::testSelectListMultiple()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 329–441 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L329-L441)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function testSelectListMultiple()
```

## Documentation

```text
Tests the 'options_select' widget (multiple select).
```

## Code

```php
  function testSelectListMultiple() {
    // Create an instance of the 'multiple values' field.
    $instance = array(
      'field_name' => $this->card_2['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
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

    // Display form: with no field data, nothing is selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoOptionSelected("edit-card-2-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 2);
    $this->assertRaw('Some dangerous &amp; unescaped markup', 'Option text was properly filtered.');

    // Submit form: select first and third options.
    $edit = array("card_2[$langcode][]" => array(0 => 0, 2 => 2));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0, 2));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertOptionSelected("edit-card-2-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 1);
    $this->assertOptionSelected("edit-card-2-$langcode", 2);

    // Submit form: select only first option.
    $edit = array("card_2[$langcode][]" => array(0 => 0));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertOptionSelected("edit-card-2-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 2);

    // Submit form: select the three options while the field accepts only 2.
    $edit = array("card_2[$langcode][]" => array(0 => 0, 1 => 1, 2 => 2));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertText('this field cannot hold more than 2 values', 'Validation error was displayed.');

    // Submit form: uncheck all options.
    $edit = array("card_2[$langcode][]" => array());
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array());

    // Test the 'None' option.

    // Check that the 'none' option has no effect if actual options are selected
    // as well.
    $edit = array("card_2[$langcode][]" => array('_none' => '_none', 0 => 0));
    $this->drupalPost('test-entity/manage/' . $entity->ftid . '/edit', $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0));

    // Check that selecting the 'none' option empties the field.
    $edit = array("card_2[$langcode][]" => array('_none' => '_none'));
    $this->drupalPost('test-entity/manage/' . $entity->ftid . '/edit', $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array());

    // A required select list does not have an empty key.
    $instance['required'] = TRUE;
    field_update_instance($instance);
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFalse($this->xpath('//select[@id=:id]//option[@value=""]', array(':id' => 'edit-card-2-' . $langcode)), 'A required select list does not have an empty key.');

    // We do not have to test that a required select list with one option is
    // auto-selected because the browser does it for us.

    // Test optgroups.

    // Use a callback function defining optgroups.
    $this->card_2['settings']['allowed_values'] = array();
    $this->card_2['settings']['allowed_values_function'] = 'list_test_allowed_values_callback';
    field_update_field($this->card_2);
    $instance['required'] = FALSE;
    field_update_instance($instance);

    // Display form: with no field data, nothing is selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoOptionSelected("edit-card-2-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 2);
    $this->assertRaw('Some dangerous &amp; unescaped markup', 'Option text was properly filtered.');
    $this->assertRaw('Group 1', 'Option groups are displayed.');

    // Submit form: select first option.
    $edit = array("card_2[$langcode][]" => array(0 => 0));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertOptionSelected("edit-card-2-$langcode", 0);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 1);
    $this->assertNoOptionSelected("edit-card-2-$langcode", 2);

    // Submit form: Unselect the option.
    $edit = array("card_2[$langcode][]" => array('_none' => '_none'));
    $this->drupalPost('test-entity/manage/' . $entity->ftid . '/edit', $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array());
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
