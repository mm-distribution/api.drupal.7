# _locale_import_one_string_db()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1119–1207 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1119-L1207)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_import_one_string_db(&$report, $langcode, $context, $source, $translation, $textgroup, $location, $mode, $plid = 0, $plural = 0)
```

## Documentation

```text
Import one string into the database.

@param $report
  Report array summarizing the number of changes done in the form:
  array(additions, deletes, skips, updates).
@param $langcode
  Language code to import string into.
@param $context
  The context of this string.
@param $source
  Source string.
@param $translation
  Translation to language specified in $langcode.
@param $textgroup
  Name of textgroup to store translation in.
@param $location
  Location value to save with source string.
@param $mode
  Import mode to use, LOCALE_IMPORT_KEEP or LOCALE_IMPORT_OVERWRITE.
@param $plid
  Optional plural ID to use.
@param $plural
  Optional plural value to use.

@return
  The string ID of the existing string modified or the new string added.
```

## Code

```php
function _locale_import_one_string_db(&$report, $langcode, $context, $source, $translation, $textgroup, $location, $mode, $plid = 0, $plural = 0) {
  $lid = db_query("SELECT lid FROM {locales_source} WHERE source = :source AND context = :context AND textgroup = :textgroup", array(':source' => $source, ':context' => $context, ':textgroup' => $textgroup))->fetchField();

  if (!empty($translation)) {
    // Skip this string unless it passes a check for dangerous code.
    // Text groups other than default still can contain HTML tags
    // (i.e. translatable blocks).
    if ($textgroup == "default" && !locale_string_is_safe($translation)) {
      $report['skips']++;
      $lid = 0;
    }
    elseif ($lid) {
      // We have this source string saved already.
      db_update('locales_source')
        ->fields(array(
          'location' => $location,
        ))
        ->condition('lid', $lid)
        ->execute();

      $exists = db_query("SELECT COUNT(lid) FROM {locales_target} WHERE lid = :lid AND language = :language", array(':lid' => $lid, ':language' => $langcode))->fetchField();

      if (!$exists) {
        // No translation in this language.
        db_insert('locales_target')
          ->fields(array(
            'lid' => $lid,
            'language' => $langcode,
            'translation' => $translation,
            'plid' => $plid,
            'plural' => $plural,
          ))
          ->execute();

        $report['additions']++;
      }
      elseif ($mode == LOCALE_IMPORT_OVERWRITE) {
        // Translation exists, only overwrite if instructed.
        db_update('locales_target')
          ->fields(array(
            'translation' => $translation,
            'plid' => $plid,
            'plural' => $plural,
          ))
          ->condition('language', $langcode)
          ->condition('lid', $lid)
          ->execute();

        $report['updates']++;
      }
    }
    else {
      // No such source string in the database yet.
      $lid = db_insert('locales_source')
        ->fields(array(
          'location' => $location,
          'source' => $source,
          'context' => (string) $context,
          'textgroup' => $textgroup,
        ))
        ->execute();

      db_insert('locales_target')
        ->fields(array(
           'lid' => $lid,
           'language' => $langcode,
           'translation' => $translation,
           'plid' => $plid,
           'plural' => $plural
        ))
        ->execute();

      $report['additions']++;
    }
  }
  elseif ($mode == LOCALE_IMPORT_OVERWRITE) {
    // Empty translation, remove existing if instructed.
    db_delete('locales_target')
      ->condition('language', $langcode)
      ->condition('lid', $lid)
      ->condition('plid', $plid)
      ->condition('plural', $plural)
      ->execute();

    $report['deletes']++;
  }

  return $lid;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
