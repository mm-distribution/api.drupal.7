# _system_date_formats_build()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3832–3897 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3832-L3897)
- **Module/theme:** system

## Signature

```php
function _system_date_formats_build()
```

## Documentation

```text
Builds and returns information about available date formats.

@return
  An associative array of date formats. The top-level keys are the names of
  the date types that the date formats belong to. The values are in turn
  associative arrays keyed by format with the following keys:
  - dfid: The date format ID.
  - format: The PHP date format string.
  - type: The machine-readable name of the date type the format belongs to.
  - locales: An array of language codes. This can include both 2 character
    language codes like 'en and 'fr' and 5 character language codes like
    'en-gb' and 'en-us'.
  - locked: A boolean indicating whether or not this date type should be
    configurable from the user interface.
  - module: The name of the module that defined this format in its
    hook_date_formats(). An empty string if the format was user-defined.
  - is_new: A boolean indicating whether or not this date type is as of yet
    unsaved in the database.
```

## Code

```php
function _system_date_formats_build() {
  $date_formats = array();

  // First handle hook_date_format_types().
  $types = _system_date_format_types_build();
  foreach ($types as $type => $info) {
    system_date_format_type_save($info);
  }

  // Get formats supplied by various contrib modules.
  $module_formats = module_invoke_all('date_formats');

  foreach ($module_formats as $module_format) {
    // System types are locked.
    $module_format['locked'] = 1;
    // If no date type is specified, assign 'custom'.
    if (!isset($module_format['type'])) {
      $module_format['type'] = 'custom';
    }
    if (!in_array($module_format['type'], array_keys($types))) {
      continue;
    }
    if (!isset($date_formats[$module_format['type']])) {
      $date_formats[$module_format['type']] = array();
    }

    // If another module already set this format, merge in the new settings.
    if (isset($date_formats[$module_format['type']][$module_format['format']])) {
      $date_formats[$module_format['type']][$module_format['format']] = array_merge_recursive($date_formats[$module_format['type']][$module_format['format']], $module_format);
    }
    else {
      // This setting will be overridden later if it already exists in the db.
      $module_format['is_new'] = TRUE;
      $date_formats[$module_format['type']][$module_format['format']] = $module_format;
    }
  }

  // Get custom formats added to the database by the end user.
  $result = db_query('SELECT df.dfid, df.format, df.type, df.locked, dfl.language FROM {date_formats} df LEFT JOIN {date_format_locale} dfl ON df.format = dfl.format AND df.type = dfl.type ORDER BY df.type, df.format');
  foreach ($result as $record) {
    // If this date type isn't set, initialise the array.
    if (!isset($date_formats[$record->type])) {
      $date_formats[$record->type] = array();
    }
    $format = (array) $record;
    $format['is_new'] = FALSE; // It's in the db, so override this setting.
    // If this format not already present, add it to the array.
    if (!isset($date_formats[$record->type][$record->format])) {
      $format['module'] = '';
      $format['locales'] = array($record->language);
      $date_formats[$record->type][$record->format] = $format;
    }
    // Format already present, so merge in settings.
    else {
      if (!empty($record->language)) {
        $format['locales'] = array_merge($date_formats[$record->type][$record->format]['locales'], array($record->language));
      }
      $date_formats[$record->type][$record->format] = array_merge($date_formats[$record->type][$record->format], $format);
    }
  }

  // Allow other modules to modify these formats.
  drupal_alter('date_formats', $date_formats);

  return $date_formats;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
