# FieldInfo::prepareInstanceWidget()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 575–596 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L575-L596)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function prepareInstanceWidget($widget, $field_type)
```

## Documentation

```text
Prepares widget properties for the current run-time context.

@param $widget
  Widget specifications as found in $instance['widget'].
@param $field_type
  The field type.

@return
  The widget properties completed for the current runtime context.
```

## Code

```php
  public function prepareInstanceWidget($widget, $field_type) {
    $field_type_info = field_info_field_types($field_type);

    // Fill in default values.
    $widget += array(
      'type' => $field_type_info['default_widget'],
      'settings' => array(),
      'weight' => 0,
    );

    $widget_type_info = field_info_widget_types($widget['type']);
    // Fall back to default formatter if formatter type is not available.
    if (!$widget_type_info) {
      $widget['type'] = $field_type_info['default_widget'];
      $widget_type_info = field_info_widget_types($widget['type']);
    }
    $widget['module'] = $widget_type_info['module'];
    // Fill in default settings for the widget.
    $widget['settings'] += field_info_widget_settings($widget['type']);

    return $widget;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
