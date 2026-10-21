# FieldUITestCase::fieldUIAddNewField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 53–76 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L53-L76)
- **Class:** [FieldUITestCase](../FieldUITestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function fieldUIAddNewField($bundle_path, $initial_edit, $field_edit = array(), $instance_edit = array())
```

## Documentation

```text
Creates a new field through the Field UI.

@param $bundle_path
  Admin path of the bundle that the new field is to be attached to.
@param $initial_edit
  $edit parameter for drupalPost() on the first step ('Manage fields'
  screen).
@param $field_edit
  $edit parameter for drupalPost() on the second step ('Field settings'
  form).
@param $instance_edit
  $edit parameter for drupalPost() on the third step ('Instance settings'
  form).
```

## Code

```php
  function fieldUIAddNewField($bundle_path, $initial_edit, $field_edit = array(), $instance_edit = array()) {
    // Use 'test_field' field type by default.
    $initial_edit += array(
      'fields[_add_new_field][type]' => 'test_field',
      'fields[_add_new_field][widget_type]' => 'test_field_widget',
    );
    $label = $initial_edit['fields[_add_new_field][label]'];
    $field_name = $initial_edit['fields[_add_new_field][field_name]'];

    // First step : 'Add new field' on the 'Manage fields' page.
    $this->drupalPost("$bundle_path/fields",  $initial_edit, t('Save'));
    $this->assertRaw(t('These settings apply to the %label field everywhere it is used.', array('%label' => $label)), 'Field settings page was displayed.');

    // Second step : 'Field settings' form.
    $this->drupalPost(NULL, $field_edit, t('Save field settings'));
    $this->assertRaw(t('Updated field %label field settings.', array('%label' => $label)), 'Redirected to instance and widget settings page.');

    // Third step : 'Instance settings' form.
    $this->drupalPost(NULL, $instance_edit, t('Save settings'));
    $this->assertRaw(t('Saved %label configuration.', array('%label' => $label)), 'Redirected to "Manage fields" page.');

    // Check that the field appears in the overview form.
    $this->assertFieldByXPath('//table[@id="field-overview"]//td[1]', $label, 'Field was created and appears in the overview page.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
