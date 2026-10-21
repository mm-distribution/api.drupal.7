# OptionsWidgetsTestCase::testOnOffCheckbox()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 446–543 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L446-L543)
- **Class:** [OptionsWidgetsTestCase](../OptionsWidgetsTestCase.md)
- **Module/theme:** options

## Signature

```php
function testOnOffCheckbox()
```

## Documentation

```text
Tests the 'options_onoff' widget.
```

## Code

```php
  function testOnOffCheckbox() {
    // Create an instance of the 'boolean' field.
    $instance = array(
      'field_name' => $this->bool['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'options_onoff',
      ),
    );
    $instance = field_create_instance($instance);
    $langcode = LANGUAGE_NONE;

    // Create an entity.
    $entity_init = field_test_create_stub_entity();
    $entity = clone $entity_init;
    $entity->is_new = TRUE;
    field_test_entity_save($entity);

    // Display form: with no field data, option is unchecked.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoFieldChecked("edit-bool-$langcode");
    $this->assertRaw('Some dangerous &amp; unescaped <strong>markup</strong>', 'Option text was properly filtered.');

    // Submit form: check the option.
    $edit = array("bool[$langcode]" => TRUE);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'bool', $langcode, array(0));

    // Display form: check that the right options are selected.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertFieldChecked("edit-bool-$langcode");

    // Submit form: uncheck the option.
    $edit = array("bool[$langcode]" => FALSE);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldValues($entity_init, 'bool', $langcode, array(1));

    // Display form: with 'off' value, option is unchecked.
    $this->drupalGet('test-entity/manage/' . $entity->ftid . '/edit');
    $this->assertNoFieldChecked("edit-bool-$langcode");

    // Create admin user.
    $admin_user = $this->drupalCreateUser(array('access content', 'administer content types', 'administer taxonomy', 'administer fields'));
    $this->drupalLogin($admin_user);

    // Create a test field instance.
    $fieldUpdate = $this->bool;
    $fieldUpdate['settings']['allowed_values'] = array(0 => 0, 1 => 'MyOnValue');
    field_update_field($fieldUpdate);
    $instance = array(
      'field_name' => $this->bool['field_name'],
      'entity_type' => 'node',
      'bundle' => 'page',
      'widget' => array(
            'type' => 'options_onoff',
            'module' => 'options',
        ),
    );
    field_create_instance($instance);

    // Go to the edit page and check if the default settings works as expected
    $fieldEditUrl = 'admin/structure/types/manage/page/fields/bool';
    $this->drupalGet($fieldEditUrl);

    $this->assertText(
      'Use field label instead of the "On value" as label ',
      'Display setting checkbox available.'
    );

    $this->assertFieldByXPath(
      '*//label[@for="edit-' . $this->bool['field_name'] . '-und" and text()="MyOnValue "]',
      TRUE,
      'Default case shows "On value"'
    );

    // Enable setting
    $edit = array('instance[widget][settings][display_label]' => 1);
    // Save the new Settings
    $this->drupalPost($fieldEditUrl, $edit, t('Save settings'));

    // Go again to the edit page and check if the setting
    // is stored and has the expected effect
    $this->drupalGet($fieldEditUrl);
    $this->assertText(
      'Use field label instead of the "On value" as label ',
      'Display setting checkbox is available'
    );
    $this->assertFieldChecked(
      'edit-instance-widget-settings-display-label',
      'Display settings checkbox checked'
    );
    $this->assertFieldByXPath(
      '*//label[@for="edit-' . $this->bool['field_name'] . '-und" and text()="' . $this->bool['field_name'] . ' "]',
      TRUE,
      'Display label changes label of the checkbox'
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
