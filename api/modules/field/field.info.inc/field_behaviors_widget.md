# field_behaviors_widget()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 317–320 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L317-L320)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_behaviors_widget($op, $instance)
```

## Documentation

```text
Determines the behavior of a widget with respect to an operation.

@param $op
  The name of the operation. Currently supported: 'default value',
  'multiple values'.
@param $instance
  The field instance array.

@return
  One of these values:
  - FIELD_BEHAVIOR_NONE: Do nothing for this operation.
  - FIELD_BEHAVIOR_CUSTOM: Use the widget's callback function.
  - FIELD_BEHAVIOR_DEFAULT: Use field.module default behavior.
```

## Code

```php
function field_behaviors_widget($op, $instance) {
  $info = field_info_widget_types($instance['widget']['type']);
  return isset($info['behaviors'][$op]) ? $info['behaviors'][$op] : FIELD_BEHAVIOR_DEFAULT;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
