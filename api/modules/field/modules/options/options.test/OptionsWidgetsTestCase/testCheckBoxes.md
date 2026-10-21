# OptionsWidgetsTestCase::testCheckBoxes()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 139–221 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L139-L221)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function testCheckBoxes()
```

## Documentation

```text
Tests the 'options_buttons' widget (multiple select).
```

## Code

```php
  function testCheckBoxes() {
    // Create an instance of the 'multiple values' field.
    $instance = array(
      'field_name' => $this->card_2['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'options_buttons',
      ),
    );
    $instance = field_create_instance($instance);
    $langcode = LANGUAGE_NONE;

    // Create an entity.
    $entity_init = field_test_create_stub_entity();
    $entity = clone $entity_init;
    $entity->is_new = TRUE;
    field_test_entity_save($entity);

    // Display form: with no field data, nothing is checked.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoFieldChecked("edit-card-2-$langcode-0");
    $this->assertNoFieldChecked("edit-card-2-$langcode-1");
    $this->assertNoFieldChecked("edit-card-2-$langcode-2");
    $this->assertRaw('Some dangerous &amp; unescaped <strong>markup</strong>', 'Option text was properly filtered.');

    // Submit form: select first and third options.
    $edit = array(
      "card_2[$langcode][0]" => TRUE,
      "card_2[$langcode][1]" => FALSE,
      "card_2[$langcode][2]" => TRUE,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0, 2));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-card-2-$langcode-0");
    $this->assertNoFieldChecked("edit-card-2-$langcode-1");
    $this->assertFieldChecked("edit-card-2-$langcode-2");

    // Submit form: select only first option.
    $edit = array(
      "card_2[$langcode][0]" => TRUE,
      "card_2[$langcode][1]" => FALSE,
      "card_2[$langcode][2]" => FALSE,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-card-2-$langcode-0");
    $this->assertNoFieldChecked("edit-card-2-$langcode-1");
    $this->assertNoFieldChecked("edit-card-2-$langcode-2");

    // Submit form: select the three options while the field accepts only 2.
    $edit = array(
      "card_2[$langcode][0]" => TRUE,
      "card_2[$langcode][1]" => TRUE,
      "card_2[$langcode][2]" => TRUE,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertText('this field cannot hold more than 2 values', 'Validation error was displayed.');

    // Submit form: uncheck all options.
    $edit = array(
      "card_2[$langcode][0]" => FALSE,
      "card_2[$langcode][1]" => FALSE,
      "card_2[$langcode][2]" => FALSE,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    // Check that the value was saved.
    $this->assertFieldValues($entity_init, 'card_2', $langcode, array());

    // Required checkbox with one option is auto-selected.
    $this->card_2['settings']['allowed_values'] = array(99 => 'Only allowed value');
    field_update_field($this->card_2);
    $instance['required'] = TRUE;
    field_update_instance($instance);
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-card-2-$langcode-99");
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
