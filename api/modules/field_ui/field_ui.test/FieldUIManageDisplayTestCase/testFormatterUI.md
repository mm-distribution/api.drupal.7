# FieldUIManageDisplayTestCase::testFormatterUI()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 488–531 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L488-L531)
- **Class:** [FieldUIManageDisplayTestCase](../FieldUIManageDisplayTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testFormatterUI()
```

## Documentation

```text
Tests formatter settings.
```

## Code

```php
  function testFormatterUI() {
    $manage_fields = 'admin/structure/types/manage/' . $this->hyphen_type;
    $manage_display = $manage_fields . '/display';

    // Create a field, and a node with some data for the field.
    $edit = array(
      'fields[_add_new_field][label]' => 'Test field',
      'fields[_add_new_field][field_name]' => 'test',
    );
    $this->fieldUIAddNewField($manage_fields, $edit);

    // Clear the test-side cache and get the saved field instance.
    field_info_cache_clear();
    $instance = field_info_instance('node', 'field_test', $this->type);
    $format = $instance['display']['default']['type'];
    $default_settings = field_info_formatter_settings($format);
    $setting_name = key($default_settings);
    $setting_value = $instance['display']['default']['settings'][$setting_name];

    // Display the "Manage display" screen and check that the expected formatter is
    // selected.
    $this->drupalGet($manage_display);
    $this->assertFieldByName('fields[field_test][type]', $format, 'The expected formatter is selected.');
    $this->assertText("$setting_name: $setting_value", 'The expected summary is displayed.');

    // Change the formatter and check that the summary is updated.
    $edit = array('fields[field_test][type]' => 'field_test_multiple', 'refresh_rows' => 'field_test');
    $this->drupalPostAJAX(NULL, $edit, array('op' => t('Refresh')));
    $format = 'field_test_multiple';
    $default_settings = field_info_formatter_settings($format);
    $setting_name = key($default_settings);
    $setting_value = $default_settings[$setting_name];
    $this->assertFieldByName('fields[field_test][type]', $format, 'The expected formatter is selected.');
    $this->assertText("$setting_name: $setting_value", 'The expected summary is displayed.');

    // Submit the form and check that the instance is updated.
    $this->drupalPost(NULL, array(), t('Save'));
    field_info_cache_clear();
    $instance = field_info_instance('node', 'field_test', $this->type);
    $current_format = $instance['display']['default']['type'];
    $current_setting_value = $instance['display']['default']['settings'][$setting_name];
    $this->assertEqual($current_format, $format, 'The formatter was updated.');
    $this->assertEqual($current_setting_value, $setting_value, 'The setting was updated.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
