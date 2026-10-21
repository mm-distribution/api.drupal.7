# system_get_date_formats()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3665–3673 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3665-L3673)
- **Module/theme:** system

## Signature

```php
function system_get_date_formats($type = NULL)
```

## Documentation

```text
Gets the list of defined date formats and attributes.

@param $type
  (optional) The date type name.

@return
  An associative array of date formats. The top-level keys are the names of
  the date types that the date formats belong to. The values are in turn
  associative arrays keyed by the format string, with the following keys:
  - dfid: The date format ID.
  - format: The format string.
  - type: The machine-readable name of the date type.
  - locales: An array of language codes. This can include both 2 character
    language codes like 'en and 'fr' and 5 character language codes like
    'en-gb' and 'en-us'.
  - locked: A boolean indicating whether or not this date type should be
    configurable from the user interface.
  - module: The name of the module that defined this date format in its
    hook_date_formats(). An empty string if the format was user-defined.
  - is_new: A boolean indicating whether or not this date type is as of yet
    unsaved in the database.
  If $type was defined, only the date formats associated with the given date
  type are returned, in a single associative array keyed by format string.
```

## Code

```php
function system_get_date_formats($type = NULL) {
  $date_formats = &drupal_static(__FUNCTION__);

  if (!isset($date_formats)) {
    $date_formats = _system_date_formats_build();
  }

  return $type ? (isset($date_formats[$type]) ? $date_formats[$type] : FALSE) : $date_formats;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
