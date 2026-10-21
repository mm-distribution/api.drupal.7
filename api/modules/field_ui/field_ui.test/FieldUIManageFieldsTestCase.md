# FieldUIManageFieldsTestCase

- **Type:** Class
- **File:** [`modules/field_ui/field_ui.test`](_file.md), lines 138–467 · [local source](../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L138-L467)
- **Module/theme:** field_ui

## Signature

```php
class FieldUIManageFieldsTestCase extends FieldUITestCase
```

## Documentation

```text
Tests the functionality of the 'Manage fields' screen.
```

## Properties

### $field_label

```php
protected $field_label;
```

### $field_name_input

```php
protected $field_name_input;
```

### $field_name

```php
protected $field_name;
```

## Methods (derived index)

- [getInfo()](FieldUIManageFieldsTestCase/getInfo.md)
- [setUp()](FieldUIManageFieldsTestCase/setUp.md)
- [testCRUDFields()](FieldUIManageFieldsTestCase/testCRUDFields.md) — Runs the field CRUD tests.
- [manageFieldsPage()](FieldUIManageFieldsTestCase/manageFieldsPage.md) — Tests the manage fields page.
- [createField()](FieldUIManageFieldsTestCase/createField.md) — Tests adding a new field.
- [updateField()](FieldUIManageFieldsTestCase/updateField.md) — Tests editing an existing field.
- [addExistingField()](FieldUIManageFieldsTestCase/addExistingField.md) — Tests adding an existing field in another content type.
- [assertFieldSettings()](FieldUIManageFieldsTestCase/assertFieldSettings.md) — Asserts field settings are as expected.
- [testDefaultValue()](FieldUIManageFieldsTestCase/testDefaultValue.md) — Tests that default value is correctly validated and saved.
- [testDeleteField()](FieldUIManageFieldsTestCase/testDeleteField.md) — Tests that deletion removes fields and instances as expected.
- [testHiddenFields()](FieldUIManageFieldsTestCase/testHiddenFields.md) — Tests that Field UI respects the 'no_ui' option in hook_field_info().
- [testRenameBundle()](FieldUIManageFieldsTestCase/testRenameBundle.md) — Tests renaming a bundle.
- [testDuplicateFieldName()](FieldUIManageFieldsTestCase/testDuplicateFieldName.md) — Tests that a duplicate field name is caught by validation.
- [testExternalDestinations()](FieldUIManageFieldsTestCase/testExternalDestinations.md) — Tests that external URLs in the 'destinations' query parameter are blocked.

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
