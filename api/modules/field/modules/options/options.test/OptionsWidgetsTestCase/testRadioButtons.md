# OptionsWidgetsTestCase::testRadioButtons()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 85–134 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L85-L134)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function testRadioButtons()
```

## Documentation

```text
Tests the 'options_buttons' widget (single select).
```

## Code

```php
  function testRadioButtons() {
    // Create an instance of the 'single value' field.
    $instance = array(
      'field_name' => $this->card_1['field_name'],
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

    // With no field data, no buttons are checked.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoFieldChecked("edit-card-1-$langcode-0");
    $this->assertNoFieldChecked("edit-card-1-$langcode-1");
    $this->assertNoFieldChecked("edit-card-1-$langcode-2");
    $this->assertRaw('Some dangerous &amp; unescaped <strong>markup</strong>', 'Option text was properly filtered.');

    // Select first option.
    $edit = array("card_1[$langcode]" => 0);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array(0));

    // Check that the selected button is checked.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-card-1-$langcode-0");
    $this->assertNoFieldChecked("edit-card-1-$langcode-1");
    $this->assertNoFieldChecked("edit-card-1-$langcode-2");

    // Unselect option.
    $edit = array("card_1[$langcode]" => '_none');
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'card_1', $langcode, array());

    // Check that required radios with one option is auto-selected.
    $this->card_1['settings']['allowed_values'] = array(99 => 'Only allowed value');
    field_update_field($this->card_1);
    $instance['required'] = TRUE;
    field_update_instance($instance);
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-card-1-$langcode-99");
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
