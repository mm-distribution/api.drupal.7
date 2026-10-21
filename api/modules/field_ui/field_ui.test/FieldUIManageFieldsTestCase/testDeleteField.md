# FieldUIManageFieldsTestCase::testDeleteField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 342–384 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L342-L384)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testDeleteField()
```

## Documentation

```text
Tests that deletion removes fields and instances as expected.
```

## Code

```php
  function testDeleteField() {
    // Create a new field.
    $bundle_path1 = 'admin/structure/types/manage/' . $this->hyphen_type;
    $edit1 = array(
      'fields[_add_new_field][label]' => $this->field_label,
      'fields[_add_new_field][field_name]' => $this->field_name_input,
    );
    $this->fieldUIAddNewField($bundle_path1, $edit1);

    // Create an additional node type.
    $type_name2 = strtolower($this->randomName(8)) . '_test';
    $type2 = $this->drupalCreateContentType(array('name' => $type_name2, 'type' => $type_name2));
    $type_name2 = $type2->type;
    $hyphen_type2 = str_replace('_', '-', $type_name2);

    // Add an instance to the second node type.
    $bundle_path2 = 'admin/structure/types/manage/' . $hyphen_type2;
    $edit2 = array(
      'fields[_add_existing_field][label]' => $this->field_label,
      'fields[_add_existing_field][field_name]' => $this->field_name,
    );
    $this->fieldUIAddExistingField($bundle_path2, $edit2);

    // Delete the first instance.
    $this->fieldUIDeleteField($bundle_path1, $this->field_name, $this->field_label, $this->type);

    // Reset the fields info.
    field_info_cache_clear();
    // Check that the field instance was deleted.
    $this->assertNull(field_info_instance('node', $this->field_name, $this->type), 'Field instance was deleted.');
    // Check that the field was not deleted
    $this->assertNotNull(field_info_field($this->field_name), 'Field was not deleted.');

    // Delete the second instance.
    $this->fieldUIDeleteField($bundle_path2, $this->field_name, $this->field_label, $type_name2);

    // Reset the fields info.
    field_info_cache_clear();
    // Check that the field instance was deleted.
    $this->assertNull(field_info_instance('node', $this->field_name, $type_name2), 'Field instance was deleted.');
    // Check that the field was deleted too.
    $this->assertNull(field_info_field($this->field_name), 'Field was deleted.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
