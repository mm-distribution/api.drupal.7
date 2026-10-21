# FieldUIManageFieldsTestCase::testHiddenFields()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 389–419 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L389-L419)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testHiddenFields()
```

## Documentation

```text
Tests that Field UI respects the 'no_ui' option in hook_field_info().
```

## Code

```php
  function testHiddenFields() {
    $bundle_path = 'admin/structure/types/manage/' . $this->hyphen_type . '/fields/';

    // Check that the field type is not available in the 'add new field' row.
    $this->drupalGet($bundle_path);
    $this->assertFalse($this->xpath('//select[@id="edit-add-new-field-type"]//option[@value="hidden_test_field"]'), "The 'add new field' select respects field types 'no_ui' property.");

    // Create a field and an instance programmatically.
    $field_name = 'hidden_test_field';
    field_create_field(array('field_name' => $field_name, 'type' => $field_name));
    $instance = array(
      'field_name' => $field_name,
      'bundle' => $this->type,
      'entity_type' => 'node',
      'label' => t('Hidden field'),
      'widget' => array('type' => 'test_field_widget'),
    );
    field_create_instance($instance);
    $this->assertTrue(field_read_instance('node', $field_name, $this->type), format_string('An instance of the field %field was created programmatically.', array('%field' => $field_name)));

    // Check that the newly added instance appears on the 'Manage Fields'
    // screen.
    $this->drupalGet($bundle_path);
    $this->assertFieldByXPath('//table[@id="field-overview"]//td[1]', $instance['label'], 'Field was created and appears in the overview page.');

    // Check that the instance does not appear in the 'add existing field' row
    // on other bundles.
    $bundle_path = 'admin/structure/types/manage/article/fields/';
    $this->drupalGet($bundle_path);
    $this->assertFalse($this->xpath('//select[@id="edit-add-existing-field-field-name"]//option[@value=:field_name]', array(':field_name' => $field_name)), "The 'add existing field' select respects field types 'no_ui' property.");
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
