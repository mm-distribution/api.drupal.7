# system_date_format_locale()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3728–3750 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3728-L3750)
- **Module/theme:** system

## Signature

```php
function system_date_format_locale($langcode = NULL, $type = NULL)
```

## Documentation

```text
Gets the appropriate date format string for a date type and locale.

@param $langcode
  (optional) Language code for the current locale. This can be a 2 character
  language code like 'en' and 'fr' or a 5 character language code like
  'en-gb' and 'en-us'.
@param $type
  (optional) The date type name.

@return
  If $type and $langcode are specified, returns the corresponding date format
  string. If only $langcode is specified, returns an array of all date
  format strings for that locale, keyed by the date type. If neither is
  specified, or if no matching formats are found, returns FALSE.
```

## Code

```php
function system_date_format_locale($langcode = NULL, $type = NULL) {
  $formats = &drupal_static(__FUNCTION__);

  if (empty($formats)) {
    $formats = array();
    $result = db_query("SELECT format, type, language FROM {date_format_locale}");
    foreach ($result as $record) {
      if (!isset($formats[$record->language])) {
        $formats[$record->language] = array();
      }
      $formats[$record->language][$record->type] = $record->format;
    }
  }

  if ($type && $langcode && !empty($formats[$langcode][$type])) {
    return $formats[$langcode][$type];
  }
  elseif ($langcode && !empty($formats[$langcode])) {
    return $formats[$langcode];
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
