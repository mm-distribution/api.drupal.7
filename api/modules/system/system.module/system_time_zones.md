# system_time_zones()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3417–3431 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3417-L3431)
- **Module/theme:** system

## Signature

```php
function system_time_zones($blank = NULL)
```

## Documentation

```text
Generate an array of time zones and their local time&date.

@param $blank
  If evaluates true, prepend an empty time zone option to the array.
```

## Code

```php
function system_time_zones($blank = NULL) {
  $zonelist = timezone_identifiers_list();
  $zones = $blank ? array('' => t('- None selected -')) : array();
  foreach ($zonelist as $zone) {
    // Because many time zones exist in PHP only for backward compatibility
    // reasons and should not be used, the list is filtered by a regular
    // expression.
    if (preg_match('!^((Africa|America|Antarctica|Arctic|Asia|Atlantic|Australia|Europe|Indian|Pacific)/|UTC$)!', $zone)) {
      $zones[$zone] = t('@zone: @date', array('@zone' => t(str_replace('_', ' ', $zone)), '@date' => format_date(REQUEST_TIME, 'custom', variable_get('date_format_long', 'l, F j, Y - H:i') . ' O', $zone)));
    }
  }
  // Sort the translated time zones alphabetically.
  asort($zones);
  return $zones;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
