# system_timezone()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3456–3462 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3456-L3462)
- **Module/theme:** system

## Signature

```php
function system_timezone($abbreviation = '', $offset = -1, $is_daylight_saving_time = NULL)
```

## Documentation

```text
Menu callback; Retrieve a JSON object containing a suggested time zone name.
```

## Code

```php
function system_timezone($abbreviation = '', $offset = -1, $is_daylight_saving_time = NULL) {
  // An abbreviation of "0" passed in the callback arguments should be
  // interpreted as the empty string.
  $abbreviation = $abbreviation ? $abbreviation : '';
  $timezone = timezone_name_from_abbr($abbreviation, intval($offset), $is_daylight_saving_time);
  drupal_json_output($timezone);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
