# field_info_widget_settings()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 777–780 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L777-L780)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_widget_settings($type)
```

## Documentation

```text
Returns a field widget's default settings.

@param $type
  A widget type name.

@return
  The widget type's default settings, as provided by
  hook_field_widget_info(), or an empty array if type or settings are
  undefined.
```

## Code

```php
function field_info_widget_settings($type) {
  $info = field_info_widget_types($type);
  return isset($info['settings']) ? $info['settings'] : array();
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
