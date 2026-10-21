# locale_date_format_save()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2428–2442 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2428-L2442)

## Signature

```php
function locale_date_format_save($langcode, $type, $format)
```

## Documentation

```text
Save locale specific date formats to the database.

@param $langcode
  Language code, can be 2 characters, e.g. 'en' or 5 characters, e.g.
  'en-CA'.
@param $type
  Date format type, e.g. 'short', 'medium'.
@param $format
  The date format string.
```

## Code

```php
function locale_date_format_save($langcode, $type, $format) {
  $locale_format = array();
  $locale_format['language'] = $langcode;
  $locale_format['type'] = $type;
  $locale_format['format'] = $format;

  $is_existing = (bool) db_query_range('SELECT 1 FROM {date_format_locale} WHERE language = :langcode AND type = :type', 0, 1, array(':langcode' => $langcode, ':type' => $type))->fetchField();
  if ($is_existing) {
    $keys = array('type', 'language');
    drupal_write_record('date_format_locale', $locale_format, $keys);
  }
  else {
    drupal_write_record('date_format_locale', $locale_format);
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
