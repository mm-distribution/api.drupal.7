# FieldDisplayAPITestCase::testFieldViewValue()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2311–2373 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2311-L2373)
- **Class:** [FieldDisplayAPITestCase](../FieldDisplayAPITestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldViewValue()
```

## Documentation

```text
Test the field_view_value() function.
```

## Code

```php
  function testFieldViewValue() {
    // No display settings: check that default display settings are used.
    $settings = field_info_formatter_settings('field_test_default');
    $setting = $settings['test_formatter_setting'];
    foreach ($this->values as $delta => $value) {
      $item = $this->entity->{$this->field_name}[LANGUAGE_NONE][$delta];
      $output = field_view_value('test_entity', $this->entity, $this->field_name, $item);
      $this->drupalSetContent(drupal_render($output));
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // Check that explicit display settings are used.
    $display = array(
      'type' => 'field_test_multiple',
      'settings' => array(
        'test_formatter_setting_multiple' => $this->randomName(),
      ),
    );
    $setting = $display['settings']['test_formatter_setting_multiple'];
    $array = array();
    foreach ($this->values as $delta => $value) {
      $item = $this->entity->{$this->field_name}[LANGUAGE_NONE][$delta];
      $output = field_view_value('test_entity', $this->entity, $this->field_name, $item, $display);
      $this->drupalSetContent(drupal_render($output));
      $this->assertText($setting . '|0:' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // Check that prepare_view steps are invoked.
    $display = array(
      'type' => 'field_test_with_prepare_view',
      'settings' => array(
        'test_formatter_setting_additional' => $this->randomName(),
      ),
    );
    $setting = $display['settings']['test_formatter_setting_additional'];
    $array = array();
    foreach ($this->values as $delta => $value) {
      $item = $this->entity->{$this->field_name}[LANGUAGE_NONE][$delta];
      $output = field_view_value('test_entity', $this->entity, $this->field_name, $item, $display);
      $this->drupalSetContent(drupal_render($output));
      $this->assertText($setting . '|' . $value['value'] . '|' . ($value['value'] + 1), format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // View mode: check that display settings specified in the instance are
    // used.
    $setting = $this->instance['display']['teaser']['settings']['test_formatter_setting'];
    foreach ($this->values as $delta => $value) {
      $item = $this->entity->{$this->field_name}[LANGUAGE_NONE][$delta];
      $output = field_view_value('test_entity', $this->entity, $this->field_name, $item, 'teaser');
      $this->drupalSetContent(drupal_render($output));
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // Unknown view mode: check that display settings for 'default' view mode
    // are used.
    $setting = $this->instance['display']['default']['settings']['test_formatter_setting'];
    foreach ($this->values as $delta => $value) {
      $item = $this->entity->{$this->field_name}[LANGUAGE_NONE][$delta];
      $output = field_view_value('test_entity', $this->entity, $this->field_name, $item, 'unknown_view_mode');
      $this->drupalSetContent(drupal_render($output));
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
