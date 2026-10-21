# locale()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 671–760 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L671-L760)
- **Module/theme:** locale

## Signature

```php
function locale($string = NULL, $context = NULL, $langcode = NULL)
```

## Documentation

```text
Provides interface translation services.

This function is called from t() to translate a string if needed.

@param $string
  A string to look up translation for. If omitted, all the
  cached strings will be returned in all languages already
  used on the page.
@param $context
  The context of this string.
@param $langcode
  Language code to use for the lookup.
```

## Code

```php
function locale($string = NULL, $context = NULL, $langcode = NULL) {
  global $language;

  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['locale'] = &drupal_static(__FUNCTION__);
  }
  $locale_t = &$drupal_static_fast['locale'];


  if (!isset($string)) {
    // Return all cached strings if no string was specified
    return $locale_t;
  }

  $langcode = isset($langcode) ? $langcode : $language->language;

  // Store database cached translations in a static variable. Only build the
  // cache after $language has been set to avoid an unnecessary cache rebuild.
  if (!isset($locale_t[$langcode]) && isset($language)) {
    $locale_t[$langcode] = array();
    // Disabling the usage of string caching allows a module to watch for
    // the exact list of strings used on a page. From a performance
    // perspective that is a really bad idea, so we have no user
    // interface for this. Be careful when turning this option off!
    if (variable_get('locale_cache_strings', 1) == 1) {
      if ($cache = cache_get('locale:' . $langcode, 'cache')) {
        $locale_t[$langcode] = $cache->data;
      }
      elseif (lock_acquire('locale_cache_' . $langcode)) {
        // Refresh database stored cache of translations for given language.
        // We only store short strings used in current version, to improve
        // performance and consume less memory.
        $result = db_query("SELECT s.source, s.context, t.translation, t.language FROM {locales_source} s LEFT JOIN {locales_target} t ON s.lid = t.lid AND t.language = :language WHERE s.textgroup = 'default' AND s.version = :version AND LENGTH(s.source) < :length", array(':language' => $langcode, ':version' => VERSION, ':length' => variable_get('locale_cache_length', 75)));
        foreach ($result as $data) {
          $locale_t[$langcode][$data->context][$data->source] = (empty($data->translation) ? TRUE : $data->translation);
        }
        cache_set('locale:' . $langcode, $locale_t[$langcode]);
        lock_release('locale_cache_' . $langcode);
      }
    }
  }

  // If we have the translation cached, skip checking the database
  if (!isset($locale_t[$langcode][$context][$string])) {

    // We do not have this translation cached, so get it from the DB.
    $translation = db_query("SELECT s.lid, t.translation, s.version FROM {locales_source} s LEFT JOIN {locales_target} t ON s.lid = t.lid AND t.language = :language WHERE s.source = :source AND s.context = :context AND s.textgroup = 'default'", array(
      ':language' => $langcode,
      ':source' => $string,
      ':context' => (string) $context,
    ))->fetchObject();
    if ($translation) {
      // We have the source string at least.
      // Cache translation string or TRUE if no translation exists.
      $locale_t[$langcode][$context][$string] = (empty($translation->translation) ? TRUE : $translation->translation);

      if ($translation->version != VERSION) {
        // This is the first use of this string under current Drupal version. Save version
        // and clear cache, to include the string into caching next time. Saved version is
        // also a string-history information for later pruning of the tables.
        db_update('locales_source')
          ->fields(array('version' => VERSION))
          ->condition('lid', $translation->lid)
          ->execute();
        cache_clear_all('locale:', 'cache', TRUE);
      }
    }
    else {
      // We don't have the source string, cache this as untranslated.
      db_merge('locales_source')
        ->insertFields(array(
          'location' => request_uri(),
          'version' => VERSION,
        ))
        ->key(array(
          'source' => $string,
          'context' => (string) $context,
          'textgroup' => 'default',
        ))
        ->execute();
      $locale_t[$langcode][$context][$string] = TRUE;
      // Clear locale cache so this string can be added in a later request.
      cache_clear_all('locale:', 'cache', TRUE);
    }
  }

  return ($locale_t[$langcode][$context][$string] === TRUE ? $string : $locale_t[$langcode][$context][$string]);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
