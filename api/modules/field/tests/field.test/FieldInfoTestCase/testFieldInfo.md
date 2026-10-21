# FieldInfoTestCase::testFieldInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1265–1384 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1265-L1384)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldInfo()
```

## Documentation

```text
Test that field types and field definitions are correcly cached.
```

## Code

```php
  function testFieldInfo() {
    // Test that field_test module's fields, widgets, and formatters show up.

    $field_test_info = field_test_field_info();
    // We need to account for the existence of user_field_info_alter().
    foreach (array_keys($field_test_info) as $name) {
      $field_test_info[$name]['instance_settings']['user_register_form'] = FALSE;
    }
    $info = field_info_field_types();
    foreach ($field_test_info as $t_key => $field_type) {
      foreach ($field_type as $key => $val) {
        $this->assertEqual($info[$t_key][$key], $val, format_string('Field type %t_key key %key is %value', array('%t_key' => $t_key, '%key' => $key, '%value' => print_r($val, TRUE))));
      }
      $this->assertEqual($info[$t_key]['module'], 'field_test',  "Field type field_test module appears");
    }

    $formatter_info = field_test_field_formatter_info();
    $info = field_info_formatter_types();
    foreach ($formatter_info as $f_key => $formatter) {
      foreach ($formatter as $key => $val) {
        $this->assertEqual($info[$f_key][$key], $val, format_string('Formatter type %f_key key %key is %value', array('%f_key' => $f_key, '%key' => $key, '%value' => print_r($val, TRUE))));
      }
      $this->assertEqual($info[$f_key]['module'], 'field_test',  "Formatter type field_test module appears");
    }

    $widget_info = field_test_field_widget_info();
    $info = field_info_widget_types();
    foreach ($widget_info as $w_key => $widget) {
      foreach ($widget as $key => $val) {
        $this->assertEqual($info[$w_key][$key], $val, format_string('Widget type %w_key key %key is %value', array('%w_key' => $w_key, '%key' => $key, '%value' => print_r($val, TRUE))));
      }
      $this->assertEqual($info[$w_key]['module'], 'field_test',  "Widget type field_test module appears");
    }

    $storage_info = field_test_field_storage_info();
    $info = field_info_storage_types();
    foreach ($storage_info as $s_key => $storage) {
      foreach ($storage as $key => $val) {
        $this->assertEqual($info[$s_key][$key], $val, format_string('Storage type %s_key key %key is %value', array('%s_key' => $s_key, '%key' => $key, '%value' => print_r($val, TRUE))));
      }
      $this->assertEqual($info[$s_key]['module'], 'field_test',  "Storage type field_test module appears");
    }

    // Verify that no unexpected instances exist.
    $instances = field_info_instances('test_entity');
    $expected = array('test_bundle' => array());
    $this->assertIdentical($instances, $expected, format_string("field_info_instances('test_entity') returns %expected.", array('%expected' => var_export($expected, TRUE))));
    $instances = field_info_instances('test_entity', 'test_bundle');
    $this->assertIdentical($instances, array(), "field_info_instances('test_entity', 'test_bundle') returns an empty array.");

    // Create a field, verify it shows up.
    $core_fields = field_info_fields();
    $field = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'test_field',
    );
    field_create_field($field);
    $fields = field_info_fields();
    $this->assertEqual(count($fields), count($core_fields) + 1, 'One new field exists');
    $this->assertEqual($fields[$field['field_name']]['field_name'], $field['field_name'], 'info fields contains field name');
    $this->assertEqual($fields[$field['field_name']]['type'], $field['type'], 'info fields contains field type');
    $this->assertEqual($fields[$field['field_name']]['module'], 'field_test', 'info fields contains field module');
    $settings = array('test_field_setting' => 'dummy test string');
    foreach ($settings as $key => $val) {
      $this->assertEqual($fields[$field['field_name']]['settings'][$key], $val, format_string('Field setting %key has correct default value %value', array('%key' => $key, '%value' => $val)));
    }
    $this->assertEqual($fields[$field['field_name']]['cardinality'], 1, 'info fields contains cardinality 1');
    $this->assertEqual($fields[$field['field_name']]['active'], 1, 'info fields contains active 1');

    // Create an instance, verify that it shows up
    $instance = array(
      'field_name' => $field['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'label' => $this->randomName(),
      'description' => $this->randomName(),
      'weight' => mt_rand(0, 127),
      // test_field has no instance settings
      'widget' => array(
        'type' => 'test_field_widget',
        'settings' => array(
          'test_setting' => 999)));
    field_create_instance($instance);

    $info = entity_get_info('test_entity');
    $instances = field_info_instances('test_entity', $instance['bundle']);
    $this->assertEqual(count($instances), 1, format_string('One instance shows up in info when attached to a bundle on a @label.', array(
      '@label' => $info['label']
    )));
    $this->assertTrue($instance < $instances[$instance['field_name']], 'Instance appears in info correctly');

    // Test a valid entity type but an invalid bundle.
    $instances = field_info_instances('test_entity', 'invalid_bundle');
    $this->assertIdentical($instances, array(), "field_info_instances('test_entity', 'invalid_bundle') returns an empty array.");

    // Test invalid entity type and bundle.
    $instances = field_info_instances('invalid_entity', $instance['bundle']);
    $this->assertIdentical($instances, array(), "field_info_instances('invalid_entity', 'test_bundle') returns an empty array.");

    // Test invalid entity type, no bundle provided.
    $instances = field_info_instances('invalid_entity');
    $this->assertIdentical($instances, array(), "field_info_instances('invalid_entity') returns an empty array.");

    // Test with an entity type that has no bundles.
    $instances = field_info_instances('user');
    $expected = array('user' => array());
    $this->assertIdentical($instances, $expected, format_string("field_info_instances('user') returns %expected.", array('%expected' => var_export($expected, TRUE))));
    $instances = field_info_instances('user', 'user');
    $this->assertIdentical($instances, array(), "field_info_instances('user', 'user') returns an empty array.");

    // Test that querying for invalid entity types does not add entries in the
    // list returned by field_info_instances().
    field_info_cache_clear();
    field_info_instances('invalid_entity', 'invalid_bundle');
    // Simulate new request by clearing static caches.
    drupal_static_reset();
    field_info_instances('invalid_entity', 'invalid_bundle');
    $instances = field_info_instances();
    $this->assertFalse(isset($instances['invalid_entity']), 'field_info_instances() does not contain entries for the invalid entity type that was queried before');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
