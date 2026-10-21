# FieldInfoTestCase::testInstancePrepare()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1420–1468 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1420-L1468)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testInstancePrepare()
```

## Documentation

```text
Test that cached instance definitions are ready for current runtime context.
```

## Code

```php
  function testInstancePrepare() {
    $field_definition = array(
      'field_name' => 'field',
      'type' => 'test_field',
    );
    field_create_field($field_definition);
    $instance_definition = array(
      'field_name' => $field_definition['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
    );
    field_create_instance($instance_definition);

    // Simulate a stored instance definition missing various settings (e.g. a
    // third-party module adding instance, widget or display settings has been
    // enabled, but existing instances do not know the new settings).
    $data = db_query('SELECT data FROM {field_config_instance} WHERE field_name = :field_name AND bundle = :bundle', array(':field_name' => $instance_definition['field_name'], ':bundle' => $instance_definition['bundle']))->fetchField();
    $data = unserialize($data);
    $data['settings'] = array();
    $data['widget']['settings'] = 'unavailable_widget';
    $data['widget']['settings'] = array();
    $data['display']['default']['type'] = 'unavailable_formatter';
    $data['display']['default']['settings'] = array();
    db_update('field_config_instance')
      ->fields(array('data' => serialize($data)))
      ->condition('field_name', $instance_definition['field_name'])
      ->condition('bundle', $instance_definition['bundle'])
      ->execute();

    field_cache_clear();

    // Read the instance back.
    $instance = field_info_instance($instance_definition['entity_type'], $instance_definition['field_name'], $instance_definition['bundle']);

    // Check that all expected instance settings are in place.
    $field_type = field_info_field_types($field_definition['type']);
    $this->assertIdentical($instance['settings'], $field_type['instance_settings'] , 'All expected instance settings are present.');

    // Check that the default widget is used and expected settings are in place.
    $this->assertIdentical($instance['widget']['type'], $field_type['default_widget'], 'Unavailable widget replaced with default widget.');
    $widget_type = field_info_widget_types($instance['widget']['type']);
    $this->assertIdentical($instance['widget']['settings'], $widget_type['settings'] , 'All expected widget settings are present.');

    // Check that display settings are set for the 'default' mode.
    $display = $instance['display']['default'];
    $this->assertIdentical($display['type'], $field_type['default_formatter'], "Formatter is set for the 'default' view mode");
    $formatter_type = field_info_formatter_types($display['type']);
    $this->assertIdentical($display['settings'], $formatter_type['settings'] , "Formatter settings are set for the 'default' view mode");
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
