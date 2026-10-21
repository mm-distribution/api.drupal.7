# FieldUITestCase::fieldUIAddExistingField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 90–107 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L90-L107)
- **Class:** [FieldUITestCase](../FieldUITestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function fieldUIAddExistingField($bundle_path, $initial_edit, $instance_edit = array())
```

## Documentation

```text
Adds an existing field through the Field UI.

@param $bundle_path
  Admin path of the bundle that the field is to be attached to.
@param $initial_edit
  $edit parameter for drupalPost() on the first step ('Manage fields'
  screen).
@param $instance_edit
  $edit parameter for drupalPost() on the second step ('Instance settings'
  form).
```

## Code

```php
  function fieldUIAddExistingField($bundle_path, $initial_edit, $instance_edit = array()) {
    // Use 'test_field_widget' by default.
    $initial_edit += array(
      'fields[_add_existing_field][widget_type]' => 'test_field_widget',
    );
    $label = $initial_edit['fields[_add_existing_field][label]'];
    $field_name = $initial_edit['fields[_add_existing_field][field_name]'];

    // First step : 'Add existing field' on the 'Manage fields' page.
    $this->drupalPost("$bundle_path/fields", $initial_edit, t('Save'));

    // Second step : 'Instance settings' form.
    $this->drupalPost(NULL, $instance_edit, t('Save settings'));
    $this->assertRaw(t('Saved %label configuration.', array('%label' => $label)), 'Redirected to "Manage fields" page.');

    // Check that the field appears in the overview form.
    $this->assertFieldByXPath('//table[@id="field-overview"]//td[1]', $label, 'Field was created and appears in the overview page.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
