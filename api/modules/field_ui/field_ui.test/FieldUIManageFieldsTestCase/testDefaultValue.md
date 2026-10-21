# FieldUIManageFieldsTestCase::testDefaultValue()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 292–337 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L292-L337)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testDefaultValue()
```

## Documentation

```text
Tests that default value is correctly validated and saved.
```

## Code

```php
  function testDefaultValue() {
    // Create a test field and instance.
    $field_name = 'test';
    $field = array(
      'field_name' => $field_name,
      'type' => 'test_field'
    );
    field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'node',
      'bundle' => $this->type,
    );
    field_create_instance($instance);

    $langcode = LANGUAGE_NONE;
    $admin_path = 'admin/structure/types/manage/' . $this->hyphen_type . '/fields/' . $field_name;
    $element_id = "edit-$field_name-$langcode-0-value";
    $element_name = "{$field_name}[$langcode][0][value]";
    $this->drupalGet($admin_path);
    $this->assertFieldById($element_id, '', 'The default value widget was empty.');

    // Check that invalid default values are rejected.
    $edit = array($element_name => '-1');
    $this->drupalPost($admin_path, $edit, t('Save settings'));
    $this->assertText("$field_name does not accept the value -1", 'Form vaildation failed.');

    // Check that the default value is saved.
    $edit = array($element_name => '1');
    $this->drupalPost($admin_path, $edit, t('Save settings'));
    $this->assertText("Saved $field_name configuration", 'The form was successfully submitted.');
    $instance = field_info_instance('node', $field_name, $this->type);
    $this->assertEqual($instance['default_value'], array(array('value' => 1)), 'The default value was correctly saved.');

    // Check that the default value shows up in the form
    $this->drupalGet($admin_path);
    $this->assertFieldById($element_id, '1', 'The default value widget was displayed with the correct value.');

    // Check that the default value can be emptied.
    $edit = array($element_name => '');
    $this->drupalPost(NULL, $edit, t('Save settings'));
    $this->assertText("Saved $field_name configuration", 'The form was successfully submitted.');
    field_info_cache_clear();
    $instance = field_info_instance('node', $field_name, $this->type);
    $this->assertEqual($instance['default_value'], NULL, 'The default value was correctly saved.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
