# system_date_format_save()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3960–3999 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3960-L3999)
- **Module/theme:** system

## Signature

```php
function system_date_format_save($date_format, $dfid = 0)
```

## Documentation

```text
Saves a date format to the database.

@param $date_format
  A date format array containing the following keys:
  - type: The name of the date type this format is associated with.
  - format: The PHP date format string.
  - locked: A boolean indicating whether or not this format should be
    configurable from the user interface.
@param $dfid
  If set, replace the existing date format having this ID with the
  information specified in $date_format.

@see system_get_date_types()
@see http://php.net/date
```

## Code

```php
function system_date_format_save($date_format, $dfid = 0) {
  $info = array();
  $info['dfid'] = $dfid;
  $info['type'] = $date_format['type'];
  $info['format'] = $date_format['format'];
  $info['locked'] = $date_format['locked'];

  // Update date_format table.
  if (!empty($date_format['is_new'])) {
    drupal_write_record('date_formats', $info);
  }
  else {
    $keys = ($dfid ? array('dfid') : array('format', 'type'));
    drupal_write_record('date_formats', $info, $keys);
  }

  // Retrieve an array of language objects for enabled languages.
  $languages = language_list('enabled');
  // This list is keyed off the value of $language->enabled; we want the ones
  // that are enabled (value of 1).
  $languages = $languages[1];

  $locale_format = array();
  $locale_format['type'] = $date_format['type'];
  $locale_format['format'] = $date_format['format'];

  // Check if the suggested language codes are configured and enabled.
  if (!empty($date_format['locales'])) {
    foreach ($date_format['locales'] as $langcode) {
      // Only proceed if language is enabled.
      if (isset($languages[$langcode])) {
        $is_existing = (bool) db_query_range('SELECT 1 FROM {date_format_locale} WHERE type = :type AND language = :language', 0, 1, array(':type' => $date_format['type'], ':language' => $langcode))->fetchField();
        if (!$is_existing) {
          $locale_format['language'] = $langcode;
          drupal_write_record('date_format_locale', $locale_format);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
