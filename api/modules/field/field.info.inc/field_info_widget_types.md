# field_info_widget_types()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 358–369 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L358-L369)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_widget_types($widget_type = NULL)
```

## Documentation

```text
Returns information about field widgets from hook_field_widget_info().

@param $widget_type
  (optional) A widget type name. If omitted, all widget types will be
  returned.

@return
  Either a single widget type description, as provided by
  hook_field_widget_info(), or an array of all existing widget types, keyed
  by widget type name.
```

## Code

```php
function field_info_widget_types($widget_type = NULL) {
  $info = _field_info_collate_types();
  $widget_types = $info['widget types'];
  if ($widget_type) {
    if (isset($widget_types[$widget_type])) {
      return $widget_types[$widget_type];
    }
  }
  else {
    return $widget_types;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
