# FieldInstanceCrudTestCase::testUpdateFieldInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3051–3104 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3051-L3104)
- **Class:** [FieldInstanceCrudTestCase](../FieldInstanceCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testUpdateFieldInstance()
```

## Documentation

```text
Test the update of a field instance.
```

## Code

```php
  function testUpdateFieldInstance() {
    field_create_instance($this->instance_definition);
    $field_type = field_info_field_types($this->field['type']);

    // Check that basic changes are saved.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $instance['required'] = !$instance['required'];
    $instance['label'] = $this->randomName();
    $instance['description'] = $this->randomName();
    $instance['settings']['test_instance_setting'] = $this->randomName();
    $instance['widget']['settings']['test_widget_setting'] =$this->randomName();
    $instance['widget']['weight']++;
    $instance['display']['default']['settings']['test_formatter_setting'] = $this->randomName();
    $instance['display']['default']['weight']++;
    field_update_instance($instance);

    $instance_new = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertEqual($instance['required'], $instance_new['required'], '"required" change is saved');
    $this->assertEqual($instance['label'], $instance_new['label'], '"label" change is saved');
    $this->assertEqual($instance['description'], $instance_new['description'], '"description" change is saved');
    $this->assertEqual($instance['widget']['settings']['test_widget_setting'], $instance_new['widget']['settings']['test_widget_setting'], 'Widget setting change is saved');
    $this->assertEqual($instance['widget']['weight'], $instance_new['widget']['weight'], 'Widget weight change is saved');
    $this->assertEqual($instance['display']['default']['settings']['test_formatter_setting'], $instance_new['display']['default']['settings']['test_formatter_setting'], 'Formatter setting change is saved');
    $this->assertEqual($instance['display']['default']['weight'], $instance_new['display']['default']['weight'], 'Widget weight change is saved');

    // Check that changing widget and formatter types updates the default settings.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $instance['widget']['type'] = 'test_field_widget_multiple';
    $instance['display']['default']['type'] = 'field_test_multiple';
    field_update_instance($instance);

    $instance_new = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertEqual($instance['widget']['type'], $instance_new['widget']['type'] , 'Widget type change is saved.');
    $settings = field_info_widget_settings($instance_new['widget']['type']);
    $this->assertIdentical($settings, array_intersect_key($instance_new['widget']['settings'], $settings) , 'Widget type change updates default settings.');
    $this->assertEqual($instance['display']['default']['type'], $instance_new['display']['default']['type'] , 'Formatter type change is saved.');
    $info = field_info_formatter_types($instance_new['display']['default']['type']);
    $settings = $info['settings'];
    $this->assertIdentical($settings, array_intersect_key($instance_new['display']['default']['settings'], $settings) , 'Changing formatter type updates default settings.');

    // Check that adding a new view mode is saved and gets default settings.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $instance['display']['teaser'] = array();
    field_update_instance($instance);

    $instance_new = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertTrue(isset($instance_new['display']['teaser']), 'Display for the new view_mode has been written.');
    $this->assertIdentical($instance_new['display']['teaser']['type'], $field_type['default_formatter'], 'Default formatter for the new view_mode has been written.');
    $info = field_info_formatter_types($instance_new['display']['teaser']['type']);
    $settings = $info['settings'];
    $this->assertIdentical($settings, $instance_new['display']['teaser']['settings'] , 'Default formatter settings for the new view_mode have been written.');

    // TODO: test failures.
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
