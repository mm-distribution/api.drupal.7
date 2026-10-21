# system_update_7013()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2121–2168 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2121-L2168)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7013()
```

## Documentation

```text
Convert default time zone offset to default time zone name.
```

## Code

```php
function system_update_7013() {
  $timezone = NULL;
  $timezones = system_time_zones();
  // If the contributed Date module set a default time zone name, use this
  // setting as the default time zone.
  if (($timezone_name = variable_get('date_default_timezone_name')) && isset($timezones[$timezone_name])) {
    $timezone = $timezone_name;
  }
  // If the contributed Event module has set a default site time zone, look up
  // the time zone name and use it as the default time zone.
  if (!$timezone && ($timezone_id = variable_get('date_default_timezone_id', 0))) {
    try {
      $timezone_name = db_query('SELECT name FROM {event_timezones} WHERE timezone = :timezone_id', array(':timezone_id' => $timezone_id))->fetchField();
      if (($timezone_name = str_replace(' ', '_', $timezone_name)) && isset($timezones[$timezone_name])) {
        $timezone = $timezone_name;
      }
    }
    catch (PDOException $e) {
      // Ignore error if event_timezones table does not exist or unexpected
      // schema found.
    }
  }

  // Check to see if timezone was overriden in update_prepare_d7_bootstrap().
  $offset = variable_get('date_temporary_timezone');
  // If not, use the default.
  if (!isset($offset)) {
    $offset = variable_get('date_default_timezone', 0);
  }

  // If the previous default time zone was a non-zero offset, guess the site's
  // intended time zone based on that offset and the server's daylight saving
  // time status.
  if (!$timezone && $offset) {
    $timezone_name = timezone_name_from_abbr('', intval($offset), date('I'));
    if ($timezone_name && isset($timezones[$timezone_name])) {
      $timezone = $timezone_name;
    }
  }
  // Otherwise, the default time zone offset was zero, which is UTC.
  if (!$timezone) {
    $timezone = 'UTC';
  }
  variable_set('date_default_timezone', $timezone);
  drupal_set_message(format_string('The default time zone has been set to %timezone. Check the <a href="@config-url">date and time configuration page</a> to configure it correctly.', array('%timezone' => $timezone, '@config-url' => url('admin/config/regional/settings'))), 'warning');
  // Remove temporary override.
  variable_del('date_temporary_timezone');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
