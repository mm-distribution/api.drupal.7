# FieldUIManageFieldsTestCase::testCRUDFields()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 166–171 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L166-L171)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testCRUDFields()
```

## Documentation

```text
Runs the field CRUD tests.

In order to act on the same fields, and not create the fields over and over
again the following tests create, update and delete the same fields.
```

## Code

```php
  function testCRUDFields() {
    $this->manageFieldsPage();
    $this->createField();
    $this->updateField();
    $this->addExistingField();
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
