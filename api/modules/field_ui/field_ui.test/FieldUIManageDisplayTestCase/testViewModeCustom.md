# FieldUIManageDisplayTestCase::testViewModeCustom()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 536–603 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L536-L603)
- **Class:** [FieldUIManageDisplayTestCase](../FieldUIManageDisplayTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function testViewModeCustom()
```

## Documentation

```text
Tests switching view modes to use custom or 'default' settings'.
```

## Code

```php
  function testViewModeCustom() {
    // Create a field, and a node with some data for the field.
    $edit = array(
      'fields[_add_new_field][label]' => 'Test field',
      'fields[_add_new_field][field_name]' => 'test',
    );
    $this->fieldUIAddNewField('admin/structure/types/manage/' . $this->hyphen_type, $edit);
    // For this test, use a formatter setting value that is an integer unlikely
    // to appear in a rendered node other than as part of the field being tested
    // (for example, unlikely to be part of the "Submitted by ... on ..." line).
    $value = 12345;
    $settings = array(
      'type' => $this->type,
      'field_test' => array(LANGUAGE_NONE => array(array('value' => $value))),
    );
    $node = $this->drupalCreateNode($settings);

    // Gather expected output values with the various formatters.
    $formatters = field_info_formatter_types();
    $output = array(
      'field_test_default' => $formatters['field_test_default']['settings']['test_formatter_setting'] . '|' . $value,
      'field_test_with_prepare_view' => $formatters['field_test_with_prepare_view']['settings']['test_formatter_setting_additional'] . '|' . $value. '|' . ($value + 1),
    );

    // Check that the field is displayed with the default formatter in 'rss'
    // mode (uses 'default'), and hidden in 'teaser' mode (uses custom settings).
    $this->assertNodeViewText($node, 'rss', $output['field_test_default'], "The field is displayed as expected in view modes that use 'default' settings.");
    $this->assertNodeViewNoText($node, 'teaser', $value, "The field is hidden in view modes that use custom settings.");

    // Change fomatter for 'default' mode, check that the field is displayed
    // accordingly in 'rss' mode.
    $edit = array(
      'fields[field_test][type]' => 'field_test_with_prepare_view',
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type . '/display', $edit, t('Save'));
    $this->assertNodeViewText($node, 'rss', $output['field_test_with_prepare_view'], "The field is displayed as expected in view modes that use 'default' settings.");

    // Specialize the 'rss' mode, check that the field is displayed the same.
    $edit = array(
      "view_modes_custom[rss]" => TRUE,
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type . '/display', $edit, t('Save'));
    $this->assertNodeViewText($node, 'rss', $output['field_test_with_prepare_view'], "The field is displayed as expected in newly specialized 'rss' mode.");

    // Set the field to 'hidden' in the view mode, check that the field is
    // hidden.
    $edit = array(
      'fields[field_test][type]' => 'hidden',
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type . '/display/rss', $edit, t('Save'));
    $this->assertNodeViewNoText($node, 'rss', $value, "The field is hidden in 'rss' mode.");

    // Set the view mode back to 'default', check that the field is displayed
    // accordingly.
    $edit = array(
      "view_modes_custom[rss]" => FALSE,
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type . '/display', $edit, t('Save'));
    $this->assertNodeViewText($node, 'rss', $output['field_test_with_prepare_view'], "The field is displayed as expected when 'rss' mode is set back to 'default' settings.");

    // Specialize the view mode again.
    $edit = array(
      "view_modes_custom[rss]" => TRUE,
    );
    $this->drupalPost('admin/structure/types/manage/' . $this->hyphen_type . '/display', $edit, t('Save'));
    // Check that the previous settings for the view mode have been kept.
    $this->assertNodeViewNoText($node, 'rss', $value, "The previous settings are kept when 'rss' mode is specialized again.");
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
