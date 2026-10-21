# FileFieldTestCase::attachFileField()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 92–108 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L92-L108)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function attachFileField($name, $entity_type, $bundle, $instance_settings = array(), $widget_settings = array())
```

## Documentation

```text
Attaches a file field to an entity.

@param $name
  The name of the new field (all lowercase), exclude the "field_" prefix.
@param $entity_type
  The entity type this field will be added to.
@param $bundle
  The bundle this field will be added to.
@param $field_settings
  A list of field settings that will be added to the defaults.
@param $instance_settings
  A list of instance settings that will be added to the instance defaults.
@param $widget_settings
  A list of widget settings that will be added to the widget defaults.
```

## Code

```php
  function attachFileField($name, $entity_type, $bundle, $instance_settings = array(), $widget_settings = array()) {
    $instance = array(
      'field_name' => $name,
      'label' => $name,
      'entity_type' => $entity_type,
      'bundle' => $bundle,
      'required' => !empty($instance_settings['required']),
      'settings' => array(),
      'widget' => array(
        'type' => 'file_generic',
        'settings' => array(),
      ),
    );
    $instance['settings'] = array_merge($instance['settings'], $instance_settings);
    $instance['widget']['settings'] = array_merge($instance['widget']['settings'], $widget_settings);
    field_create_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
