# FieldUIManageFieldsTestCase::addExistingField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 246–262 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L246-L262)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function addExistingField()
```

## Documentation

```text
Tests adding an existing field in another content type.
```

## Code

```php
  function addExistingField() {
    // Check "Add existing field" appears.
    $this->drupalGet('admin/structure/types/manage/page/fields');
    $this->assertRaw(t('Add existing field'), '"Add existing field" was found.');

    // Check that the list of options respects entity type restrictions on
    // fields. The 'comment' field is restricted to the 'comment' entity type
    // and should not appear in the list.
    $this->assertFalse($this->xpath('//select[@id="edit-add-existing-field-field-name"]//option[@value="comment"]'), 'The list of options respects entity type restrictions.');

    // Add a new field based on an existing field.
    $edit = array(
      'fields[_add_existing_field][label]' => $this->field_label . '_2',
      'fields[_add_existing_field][field_name]' => $this->field_name,
    );
    $this->fieldUIAddExistingField("admin/structure/types/manage/page", $edit);
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
