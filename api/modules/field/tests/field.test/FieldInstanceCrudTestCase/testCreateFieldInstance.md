# FieldInstanceCrudTestCase::testCreateFieldInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2957–3035 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2957-L3035)
- **Class:** [FieldInstanceCrudTestCase](../FieldInstanceCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testCreateFieldInstance()
```

## Documentation

```text
Test the creation of a field instance.
```

## Code

```php
  function testCreateFieldInstance() {
    field_create_instance($this->instance_definition);

    // Read the raw record from the {field_config_instance} table.
    $result = db_query('SELECT * FROM {field_config_instance} WHERE field_name = :field_name AND bundle = :bundle', array(':field_name' => $this->instance_definition['field_name'], ':bundle' => $this->instance_definition['bundle']));
    $record = $result->fetchAssoc();
    $record['data'] = unserialize($record['data']);

    $field_type = field_info_field_types($this->field['type']);
    $widget_type = field_info_widget_types($field_type['default_widget']);
    $formatter_type = field_info_formatter_types($field_type['default_formatter']);

    // Check that default values are set.
    $this->assertIdentical($record['data']['required'], FALSE, 'Required defaults to false.');
    $this->assertIdentical($record['data']['label'], $this->instance_definition['field_name'], 'Label defaults to field name.');
    $this->assertIdentical($record['data']['description'], '', 'Description defaults to empty string.');
    $this->assertIdentical($record['data']['widget']['type'], $field_type['default_widget'], 'Default widget has been written.');
    $this->assertTrue(isset($record['data']['display']['default']), 'Display for "full" view_mode has been written.');
    $this->assertIdentical($record['data']['display']['default']['type'], $field_type['default_formatter'], 'Default formatter for "full" view_mode has been written.');

    // Check that default settings are set.
    $this->assertIdentical($record['data']['settings'], $field_type['instance_settings'] , 'Default instance settings have been written.');
    $this->assertIdentical($record['data']['widget']['settings'], $widget_type['settings'] , 'Default widget settings have been written.');
    $this->assertIdentical($record['data']['display']['default']['settings'], $formatter_type['settings'], 'Default formatter settings for "full" view_mode have been written.');

    // Guarantee that the field/bundle combination is unique.
    try {
      field_create_instance($this->instance_definition);
      $this->fail(t('Cannot create two instances with the same field / bundle combination.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create two instances with the same field / bundle combination.'));
    }

    // Check that the specified field exists.
    try {
      $this->instance_definition['field_name'] = $this->randomName();
      field_create_instance($this->instance_definition);
      $this->fail(t('Cannot create an instance of a non-existing field.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create an instance of a non-existing field.'));
    }

    // Create a field restricted to a specific entity type.
    $field_restricted = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'test_field',
      'entity_types' => array('test_cacheable_entity'),
    );
    field_create_field($field_restricted);

    // Check that an instance can be added to an entity type allowed
    // by the field.
    try {
      $instance = $this->instance_definition;
      $instance['field_name'] = $field_restricted['field_name'];
      $instance['entity_type'] = 'test_cacheable_entity';
      field_create_instance($instance);
      $this->pass(t('Can create an instance on an entity type allowed by the field.'));
    }
    catch (FieldException $e) {
      $this->fail(t('Can create an instance on an entity type allowed by the field.'));
    }

    // Check that an instance cannot be added to an entity type
    // forbidden by the field.
    try {
      $instance = $this->instance_definition;
      $instance['field_name'] = $field_restricted['field_name'];
      field_create_instance($instance);
      $this->fail(t('Cannot create an instance on an entity type forbidden by the field.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create an instance on an entity type forbidden by the field.'));
    }

    // TODO: test other failures.
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
