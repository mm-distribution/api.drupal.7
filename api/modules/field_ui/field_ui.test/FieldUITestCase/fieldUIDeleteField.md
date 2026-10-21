# FieldUITestCase::fieldUIDeleteField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 121–132 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L121-L132)
- **Class:** [FieldUITestCase](../FieldUITestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function fieldUIDeleteField($bundle_path, $field_name, $label, $bundle_label)
```

## Documentation

```text
Deletes a field instance through the Field UI.

@param $bundle_path
  Admin path of the bundle that the field instance is to be deleted from.
@param $field_name
  The name of the field.
@param $label
  The label of the field.
@param $bundle_label
  The label of the bundle.
```

## Code

```php
  function fieldUIDeleteField($bundle_path, $field_name, $label, $bundle_label) {
    // Display confirmation form.
    $this->drupalGet("$bundle_path/fields/$field_name/delete");
    $this->assertRaw(t('Are you sure you want to delete the field %label', array('%label' => $label)), 'Delete confirmation was found.');

    // Submit confirmation form.
    $this->drupalPost(NULL, array(), t('Delete'));
    $this->assertRaw(t('The field %label has been deleted from the %type content type.', array('%label' => $label, '%type' => $bundle_label)), 'Delete message was found.');

    // Check that the field does not appear in the overview form.
    $this->assertNoFieldByXPath('//table[@id="field-overview"]//span[@class="label-field"]', $label, 'Field does not appear in the overview page.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
