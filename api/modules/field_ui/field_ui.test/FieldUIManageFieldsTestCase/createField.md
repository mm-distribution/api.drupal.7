# FieldUIManageFieldsTestCase::createField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 204–218 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L204-L218)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function createField()
```

## Documentation

```text
Tests adding a new field.

@todo Assert properties can bet set in the form and read back in $field and
$instances.
```

## Code

```php
  function createField() {
    // Create a test field.
    $edit = array(
      'fields[_add_new_field][label]' => $this->field_label,
      'fields[_add_new_field][field_name]' => $this->field_name_input,
    );
    $this->fieldUIAddNewField('admin/structure/types/manage/' . $this->hyphen_type, $edit);

    // Assert the field appears in the "add existing field" section for
    // different entity types; e.g. if a field was added in a node entity, it
    // should also appear in the 'taxonomy term' entity.
    $vocabulary = taxonomy_vocabulary_load(1);
    $this->drupalGet('admin/structure/taxonomy/' . $vocabulary->machine_name . '/fields');
    $this->assertTrue($this->xpath('//select[@name="fields[_add_existing_field][field_name]"]//option[@value="' . $this->field_name . '"]'), 'Existing field was found in account settings.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
