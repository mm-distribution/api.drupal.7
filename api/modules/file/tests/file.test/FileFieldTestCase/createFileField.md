# FileFieldTestCase::createFileField()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 63–74 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L63-L74)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function createFileField($name, $type_name, $field_settings = array(), $instance_settings = array(), $widget_settings = array())
```

## Documentation

```text
Creates a new file field.

@param $name
  The name of the new field (all lowercase), exclude the "field_" prefix.
@param $type_name
  The node type that this field will be added to.
@param $field_settings
  A list of field settings that will be added to the defaults.
@param $instance_settings
  A list of instance settings that will be added to the instance defaults.
@param $widget_settings
  A list of widget settings that will be added to the widget defaults.
```

## Code

```php
  function createFileField($name, $type_name, $field_settings = array(), $instance_settings = array(), $widget_settings = array()) {
    $field = array(
      'field_name' => $name,
      'type' => 'file',
      'settings' => array(),
      'cardinality' => !empty($field_settings['cardinality']) ? $field_settings['cardinality'] : 1,
    );
    $field['settings'] = array_merge($field['settings'], $field_settings);
    field_create_field($field);

    $this->attachFileField($name, 'node', $type_name, $instance_settings, $widget_settings);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
