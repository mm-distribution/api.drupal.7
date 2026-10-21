# locale_get_localized_date_format()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2453–2500 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2453-L2500)

## Signature

```php
function locale_get_localized_date_format($languages)
```

## Documentation

```text
Select locale date format details from database.

@param $languages
  An array of language codes.

@return
  An array of date formats.
```

## Code

```php
function locale_get_localized_date_format($languages) {
  $formats = array();

  // Get list of different format types.
  $format_types = system_get_date_types();
  $short_default = variable_get('date_format_short', 'm/d/Y - H:i');

  // Loop through each language until we find one with some date formats
  // configured.
  foreach ($languages as $language) {
    $date_formats = system_date_format_locale($language);
    if (!empty($date_formats)) {
      // We have locale-specific date formats, so check for their types. If
      // we're missing a type, use the default setting instead.
      foreach ($format_types as $type => $type_info) {
        // If format exists for this language, use it.
        if (!empty($date_formats[$type])) {
          $formats['date_format_' . $type] = $date_formats[$type];
        }
        // Otherwise get default variable setting. If this is not set, default
        // to the short format.
        else {
          $formats['date_format_' . $type] = variable_get('date_format_' . $type, $short_default);
        }
      }

      // Return on the first match.
      return $formats;
    }
  }

  // No locale specific formats found, so use defaults.
  $system_types = array('short', 'medium', 'long');
  // Handle system types separately as they have defaults if no variable exists.
  $formats['date_format_short'] = $short_default;
  $formats['date_format_medium'] = variable_get('date_format_medium', 'D, m/d/Y - H:i');
  $formats['date_format_long'] = variable_get('date_format_long', 'l, F j, Y - H:i');

  // For non-system types, get the default setting, otherwise use the short
  // format.
  foreach ($format_types as $type => $type_info) {
    if (!in_array($type, $system_types)) {
      $formats['date_format_' . $type] = variable_get('date_format_' . $type, $short_default);
    }
  }

  return $formats;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
