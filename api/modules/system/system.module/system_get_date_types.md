# system_get_date_types()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3611–3619 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3611-L3619)
- **Module/theme:** system

## Signature

```php
function system_get_date_types($type = NULL)
```

## Documentation

```text
Gets the list of available date types and attributes.

@param $type
  (optional) The date type name.

@return
  An associative array of date type information keyed by the date type name.
  Each date type information array has the following elements:
  - type: The machine-readable name of the date type.
  - title: The human-readable name of the date type.
  - locked: A boolean indicating whether or not this date type should be
    configurable from the user interface.
  - module: The name of the module that defined this date type in its
    hook_date_format_types(). An empty string if the date type was
    user-defined.
  - is_new: A boolean indicating whether or not this date type is as of yet
    unsaved in the database.
  If $type was defined, only a single associative array with the above
  elements is returned.
```

## Code

```php
function system_get_date_types($type = NULL) {
  $types = &drupal_static(__FUNCTION__);

  if (!isset($types)) {
    $types = _system_date_format_types_build();
  }

  return $type ? (isset($types[$type]) ? $types[$type] : FALSE) : $types;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
