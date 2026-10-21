# FieldUIManageFieldsTestCase::manageFieldsPage()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 176–196 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L176-L196)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function manageFieldsPage()
```

## Documentation

```text
Tests the manage fields page.
```

## Code

```php
  function manageFieldsPage() {
    $this->drupalGet('admin/structure/types/manage/' . $this->hyphen_type . '/fields');
    // Check all table columns.
    $table_headers = array(
      t('Label'),
      t('Machine name'),
      t('Field type'),
      t('Widget'),
      t('Operations'),
    );
    foreach ($table_headers as $table_header) {
      // We check that the label appear in the table headings.
      $this->assertRaw($table_header . '</th>', format_string('%table_header table header was found.', array('%table_header' => $table_header)));
    }

    // "Add new field" and "Add existing field" aren't a table heading so just
    // test the text.
    foreach (array('Add new field', 'Add existing field') as $element) {
      $this->assertText($element, format_string('"@element" was found.', array('@element' => $element)));
    }
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
