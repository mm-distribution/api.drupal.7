# _locale_import_po()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 669–705 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L669-L705)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_po($file, $langcode, $mode, $group = NULL)
```

## Documentation

```text
Parses Gettext Portable Object file information and inserts into database

@param $file
  Drupal file object corresponding to the PO file to import.
@param $langcode
  Language code.
@param $mode
  Should existing translations be replaced LOCALE_IMPORT_KEEP or
  LOCALE_IMPORT_OVERWRITE.
@param $group
  Text group to import PO file into (eg. 'default' for interface
  translations).
```

## Code

```php
function _locale_import_po($file, $langcode, $mode, $group = NULL) {
  // Check if we have the language already in the database.
  if (!db_query("SELECT COUNT(language) FROM {languages} WHERE language = :language", array(':language' => $langcode))->fetchField()) {
    drupal_set_message(t('The language selected for import is not supported.'), 'error');
    return FALSE;
  }

  // Get strings from file (returns on failure after a partial import, or on success)
  $status = _locale_import_read_po('db-store', $file, $mode, $langcode, $group);
  if ($status === FALSE) {
    // Error messages are set in _locale_import_read_po().
    return FALSE;
  }

  // Get status information on import process.
  list($header_done, $additions, $updates, $deletes, $skips) = _locale_import_one_string('db-report');

  if (!$header_done) {
    drupal_set_message(t('The translation file %filename appears to have a missing or malformed header.', array('%filename' => $file->filename)), 'error');
  }

  // Clear cache and force refresh of JavaScript translations.
  _locale_invalidate_js($langcode);
  cache_clear_all('locale:', 'cache', TRUE);

  // Rebuild the menu, strings may have changed.
  menu_rebuild();

  drupal_set_message(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => $additions, '%update' => $updates, '%delete' => $deletes)));
  watchdog('locale', 'Imported %file into %locale: %number new strings added, %update updated and %delete removed.', array('%file' => $file->filename, '%locale' => $langcode, '%number' => $additions, '%update' => $updates, '%delete' => $deletes));
  if ($skips) {
    $skip_message = format_plural($skips, 'One translation string was skipped because it contains disallowed HTML.', '@count translation strings were skipped because they contain disallowed HTML.');
    drupal_set_message($skip_message);
    watchdog('locale', '@count disallowed HTML string(s) in %file', array('@count' => $skips, '%file' => $file->uri), WATCHDOG_WARNING);
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
