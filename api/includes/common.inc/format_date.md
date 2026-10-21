# format_date()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2081–2150 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2081-L2150)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_date($timestamp, $type = 'medium', $format = '', $timezone = NULL, $langcode = NULL)
```

## Documentation

```text
Formats a date, using a date type or a custom date format string.

@param $timestamp
  A UNIX timestamp to format.
@param $type
  (optional) The format to use, one of:
  - 'short', 'medium', or 'long' (the corresponding built-in date formats).
  - The name of a date type defined by a module in hook_date_format_types(),
    if it's been assigned a format.
  - The machine name of an administrator-defined date format.
  - 'custom', to use $format.
  Defaults to 'medium'.
@param $format
  (optional) If $type is 'custom', a PHP date format string suitable for
  input to date(). Use a backslash to escape ordinary text, so it does not
  get interpreted as date format characters.
@param $timezone
  (optional) Time zone identifier, as described at
  http://php.net/manual/timezones.php Defaults to the time zone used to
  display the page.
@param $langcode
  (optional) Language code to translate to. Defaults to the language used to
  display the page.

@return
  A translated date string in the requested format.
```

## Code

```php
function format_date($timestamp, $type = 'medium', $format = '', $timezone = NULL, $langcode = NULL) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['timezones'] = &drupal_static(__FUNCTION__);
  }
  $timezones = &$drupal_static_fast['timezones'];

  if (!isset($timezone)) {
    $timezone = date_default_timezone_get();
  }
  // Store DateTimeZone objects in an array rather than repeatedly
  // constructing identical objects over the life of a request.
  if (!isset($timezones[$timezone])) {
    $timezones[$timezone] = timezone_open($timezone);
  }

  // Use the default langcode if none is set.
  global $language;
  if (empty($langcode)) {
    $langcode = isset($language->language) ? $language->language : 'en';
  }

  switch ($type) {
    case 'short':
      $format = variable_get('date_format_short', 'm/d/Y - H:i');
      break;

    case 'long':
      $format = variable_get('date_format_long', 'l, F j, Y - H:i');
      break;

    case 'custom':
      // No change to format.
      break;

    case 'medium':
    default:
      // Retrieve the format of the custom $type passed.
      if ($type != 'medium') {
        $format = variable_get('date_format_' . $type, '');
      }
      // Fall back to 'medium'.
      if ($format === '') {
        $format = variable_get('date_format_medium', 'D, m/d/Y - H:i');
      }
      break;
  }

  // Create a DateTime object from the timestamp.
  $date_time = date_create('@' . $timestamp);
  // Set the time zone for the DateTime object.
  date_timezone_set($date_time, $timezones[$timezone]);

  // Encode markers that should be translated. 'A' becomes '\xEF\AA\xFF'.
  // xEF and xFF are invalid UTF-8 sequences, and we assume they are not in the
  // input string.
  // Paired backslashes are isolated to prevent errors in read-ahead evaluation.
  // The read-ahead expression ensures that A matches, but not \A.
  $format = preg_replace(array('/\\\\\\\\/', '/(?<!\\\\)([AaeDlMTF])/'), array("\xEF\\\\\\\\\xFF", "\xEF\\\\\$1\$1\xFF"), $format);

  // Call date_format().
  $format = date_format($date_time, $format);

  // Pass the langcode to _format_date_callback().
  _format_date_callback(NULL, $langcode);

  // Translate the marked sequences.
  return preg_replace_callback('/\xEF([AaeDlMTF]?)(.*?)\xFF/', '_format_date_callback', $format);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
