# FieldUIManageFieldsTestCase::updateField()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 223–241 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L223-L241)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function updateField()
```

## Documentation

```text
Tests editing an existing field.
```

## Code

```php
  function updateField() {
    // Go to the field edit page.
    $this->drupalGet('admin/structure/types/manage/' . $this->hyphen_type . '/fields/' . $this->field_name);

    // Populate the field settings with new settings.
    $string = 'updated dummy test string';
    $edit = array(
      'field[settings][test_field_setting]' => $string,
      'instance[settings][test_instance_setting]' => $string,
      'instance[widget][settings][test_widget_setting]' => $string,
    );
    $this->drupalPost(NULL, $edit, t('Save settings'));

    // Assert the field settings are correct.
    $this->assertFieldSettings($this->type, $this->field_name, $string);

    // Assert redirection back to the "manage fields" page.
    $this->assertText(t('Saved @label configuration.', array('@label' => $this->field_label)), 'Redirected to "Manage fields" page.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
