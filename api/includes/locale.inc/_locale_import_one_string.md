# _locale_import_one_string()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1015–1089 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1015-L1089)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_one_string($op, $value = NULL, $mode = NULL, $lang = NULL, $file = NULL, $group = 'default')
```

## Documentation

```text
Imports a string into the database

@param $op
  Operation to perform: 'db-store', 'db-report', 'mem-store' or 'mem-report'.
@param $value
  Details of the string stored.
@param $mode
  Should existing translations be replaced LOCALE_IMPORT_KEEP or
  LOCALE_IMPORT_OVERWRITE.
@param $lang
  Language to store the string in.
@param $file
  Object representation of file being imported, only required when op is
  'db-store'.
@param $group
  Text group to import PO file into (eg. 'default' for interface
  translations).
```

## Code

```php
function _locale_import_one_string($op, $value = NULL, $mode = NULL, $lang = NULL, $file = NULL, $group = 'default') {
  $report = &drupal_static(__FUNCTION__, array('additions' => 0, 'updates' => 0, 'deletes' => 0, 'skips' => 0));
  $header_done = &drupal_static(__FUNCTION__ . ':header_done', FALSE);
  $strings = &drupal_static(__FUNCTION__ . ':strings', array());

  switch ($op) {
    // Return stored strings
    case 'mem-report':
      return $strings;

    // Store string in memory (only supports single strings)
    case 'mem-store':
      $strings[isset($value['msgctxt']) ? $value['msgctxt'] : ''][$value['msgid']] = $value['msgstr'];
      return;

    // Called at end of import to inform the user
    case 'db-report':
      return array($header_done, $report['additions'], $report['updates'], $report['deletes'], $report['skips']);

    // Store the string we got in the database.
    case 'db-store':
      // We got header information.
      if ($value['msgid'] == '') {
        $languages = language_list();
        if (($mode != LOCALE_IMPORT_KEEP) || empty($languages[$lang]->plurals)) {
          // Since we only need to parse the header if we ought to update the
          // plural formula, only run this if we don't need to keep existing
          // data untouched or if we don't have an existing plural formula.
          $header = _locale_import_parse_header($value['msgstr']);

          // Get and store the plural formula if available.
          if (isset($header["Plural-Forms"]) && $p = _locale_import_parse_plural_forms($header["Plural-Forms"], $file->uri)) {
            list($nplurals, $plural) = $p;
            db_update('languages')
              ->fields(array(
                'plurals' => $nplurals,
                'formula' => $plural,
              ))
              ->condition('language', $lang)
              ->execute();
          }
        }
        $header_done = TRUE;
      }

      else {
        // Some real string to import.
        $comments = _locale_import_shorten_comments(empty($value['#']) ? array() : $value['#']);

        if (strpos($value['msgid'], "\0")) {
          // This string has plural versions.
          $english = explode("\0", $value['msgid'], 2);
          $entries = array_keys($value['msgstr']);
          for ($i = 3; $i <= count($entries); $i++) {
            $english[] = $english[1];
          }
          $translation = array_map('_locale_import_append_plural', $value['msgstr'], $entries);
          $english = array_map('_locale_import_append_plural', $english, $entries);
          foreach ($translation as $key => $trans) {
            if ($key == 0) {
              $plid = 0;
            }
            $plid = _locale_import_one_string_db($report, $lang, isset($value['msgctxt']) ? $value['msgctxt'] : '', $english[$key], $trans, $group, $comments, $mode, $plid, $key);
          }
        }

        else {
          // A simple string to import.
          $english = $value['msgid'];
          $translation = $value['msgstr'];
          _locale_import_one_string_db($report, $lang, isset($value['msgctxt']) ? $value['msgctxt'] : '', $english, $translation, $group, $comments, $mode);
        }
      }
  } // end of db-store operation
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
