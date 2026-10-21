# ImageFieldTestCase::createImageField()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 58–83 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L58-L83)
- **Class:** [ImageFieldTestCase](../ImageFieldTestCase.md)
- **Module/theme:** image

## Signature

```php
function createImageField($name, $type_name, $field_settings = array(), $instance_settings = array(), $widget_settings = array())
```

## Documentation

```text
Create a new image field.

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
  function createImageField($name, $type_name, $field_settings = array(), $instance_settings = array(), $widget_settings = array()) {
    $field = array(
      'field_name' => $name,
      'type' => 'image',
      'settings' => array(),
      'cardinality' => !empty($field_settings['cardinality']) ? $field_settings['cardinality'] : 1,
    );
    $field['settings'] = array_merge($field['settings'], $field_settings);
    field_create_field($field);

    $instance = array(
      'field_name' => $field['field_name'],
      'entity_type' => 'node',
      'label' => $name,
      'bundle' => $type_name,
      'required' => !empty($instance_settings['required']),
      'settings' => array(),
      'widget' => array(
        'type' => 'image_image',
        'settings' => array(),
      ),
    );
    $instance['settings'] = array_merge($instance['settings'], $instance_settings);
    $instance['widget']['settings'] = array_merge($instance['widget']['settings'], $widget_settings);
    return field_create_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
