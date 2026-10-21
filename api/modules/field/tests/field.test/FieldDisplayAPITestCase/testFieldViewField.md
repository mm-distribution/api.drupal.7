# FieldDisplayAPITestCase::testFieldViewField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2237–2306 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2237-L2306)
- **Class:** [FieldDisplayAPITestCase](../FieldDisplayAPITestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldViewField()
```

## Documentation

```text
Test the field_view_field() function.
```

## Code

```php
  function testFieldViewField() {
    // No display settings: check that default display settings are used.
    $output = field_view_field('test_entity', $this->entity, $this->field_name);
    $this->drupalSetContent(drupal_render($output));
    $settings = field_info_formatter_settings('field_test_default');
    $setting = $settings['test_formatter_setting'];
    $this->assertText($this->label, 'Label was displayed.');
    foreach ($this->values as $delta => $value) {
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // Check that explicit display settings are used.
    $display = array(
      'label' => 'hidden',
      'type' => 'field_test_multiple',
      'settings' => array(
        'test_formatter_setting_multiple' => $this->randomName(),
        'alter' => TRUE,
      ),
    );
    $output = field_view_field('test_entity', $this->entity, $this->field_name, $display, LANGUAGE_NONE);
    $this->drupalSetContent(drupal_render($output));
    $setting = $display['settings']['test_formatter_setting_multiple'];
    $this->assertNoText($this->label, 'Label was not displayed.');
    $this->assertText('field_test_field_attach_view_alter', 'Alter fired, display passed.');
    $this->assertText('field language is ' . LANGUAGE_NONE, 'Language is placed onto the context.');
    $array = array();
    foreach ($this->values as $delta => $value) {
      $array[] = $delta . ':' . $value['value'];
    }
    $this->assertText($setting . '|' . implode('|', $array), 'Values were displayed with expected setting.');

    // Check the prepare_view steps are invoked.
    $display = array(
      'label' => 'hidden',
      'type' => 'field_test_with_prepare_view',
      'settings' => array(
        'test_formatter_setting_additional' => $this->randomName(),
      ),
    );
    $output = field_view_field('test_entity', $this->entity, $this->field_name, $display);
    $view = drupal_render($output);
    $this->drupalSetContent($view);
    $setting = $display['settings']['test_formatter_setting_additional'];
    $this->assertNoText($this->label, 'Label was not displayed.');
    $this->assertNoText('field_test_field_attach_view_alter', 'Alter not fired.');
    foreach ($this->values as $delta => $value) {
      $this->assertText($setting . '|' . $value['value'] . '|' . ($value['value'] + 1), format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // View mode: check that display settings specified in the instance are
    // used.
    $output = field_view_field('test_entity', $this->entity, $this->field_name, 'teaser');
    $this->drupalSetContent(drupal_render($output));
    $setting = $this->instance['display']['teaser']['settings']['test_formatter_setting'];
    $this->assertText($this->label, 'Label was displayed.');
    foreach ($this->values as $delta => $value) {
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }

    // Unknown view mode: check that display settings for 'default' view mode
    // are used.
    $output = field_view_field('test_entity', $this->entity, $this->field_name, 'unknown_view_mode');
    $this->drupalSetContent(drupal_render($output));
    $setting = $this->instance['display']['default']['settings']['test_formatter_setting'];
    $this->assertText($this->label, 'Label was displayed.');
    foreach ($this->values as $delta => $value) {
      $this->assertText($setting . '|' . $value['value'], format_string('Value @delta was displayed with expected setting.', array('@delta' => $delta)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
