# _locale_rebuild_js()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2042–2171 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2042-L2171)
- **Topics:** [locale-api-seek](../../topics/locale-api-seek.md)

## Signature

```php
function _locale_rebuild_js($langcode = NULL)
```

## Documentation

```text
(Re-)Creates the JavaScript translation file for a language.

@param $language
  The language, the translation file should be (re)created for.
```

## Code

```php
function _locale_rebuild_js($langcode = NULL) {
  if (!isset($langcode)) {
    global $language;
  }
  else {
    // Get information about the locale.
    $languages = language_list();
    $language = $languages[$langcode];
  }

  // Construct the array for JavaScript translations.
  // Only add strings with a translation to the translations array.
  $result = db_query("SELECT s.lid, s.source, s.context, t.translation FROM {locales_source} s INNER JOIN {locales_target} t ON s.lid = t.lid AND t.language = :language WHERE s.location LIKE '%.js%' AND s.textgroup = :textgroup", array(':language' => $language->language, ':textgroup' => 'default'));

  $translations = array();
  foreach ($result as $data) {
    $translations[$data->context][$data->source] = $data->translation;
  }

  // Include custom string overrides.
  $custom_strings = variable_get('locale_custom_strings_' . $language->language, array());
  foreach ($custom_strings as $context => $strings) {
    foreach ($strings as $source => $translation) {
      $translations[$context][$source] = $translation;
    }
  }

  // Construct the JavaScript file, if there are translations.
  $data_hash = NULL;
  $data = $status = '';
  if (!empty($translations)) {

    $data = "Drupal.locale = { ";

    if (!empty($language->formula)) {
      $data .= "'pluralFormula': function (\$n) { return Number({$language->formula}); }, ";
    }

    $data .= "'strings': " . drupal_json_encode($translations) . " };";
    $data_hash = drupal_hash_base64($data);
  }

  // Construct the filepath where JS translation files are stored.
  // There is (on purpose) no front end to edit that variable.
  $dir = 'public://' . variable_get('locale_js_directory', 'languages');

  // Delete old file, if we have no translations anymore, or a different file to be saved.
  $changed_hash = $language->javascript != $data_hash;
  if (!empty($language->javascript) && (!$data || $changed_hash)) {
    file_unmanaged_delete($dir . '/' . $language->language . '_' . $language->javascript . '.js');
    $language->javascript = '';
    $status = 'deleted';
  }

  // Only create a new file if the content has changed or the original file got
  // lost.
  $dest = $dir . '/' . $language->language . '_' . $data_hash . '.js';
  if ($data && ($changed_hash || !file_exists($dest))) {
    // Ensure that the directory exists and is writable, if possible.
    file_prepare_directory($dir, FILE_CREATE_DIRECTORY);

    // Save the file.
    if (file_unmanaged_save_data($data, $dest)) {
      $language->javascript = $data_hash;
      // If we deleted a previous version of the file and we replace it with a
      // new one we have an update.
      if ($status == 'deleted') {
        $status = 'updated';
      }
      // If the file did not exist previously and the data has changed we have
      // a fresh creation.
      elseif ($changed_hash) {
        $status = 'created';
      }
      // If the data hash is unchanged the translation was lost and has to be
      // rebuilt.
      else {
        $status = 'rebuilt';
      }
    }
    else {
      $language->javascript = '';
      $status = 'error';
    }
  }

  // Save the new JavaScript hash (or an empty value if the file just got
  // deleted). Act only if some operation was executed that changed the hash
  // code.
  if ($status && $changed_hash) {
    db_update('languages')
      ->fields(array(
        'javascript' => $language->javascript,
      ))
      ->condition('language', $language->language)
      ->execute();

    // Update the default language variable if the default language has been altered.
    // This is necessary to keep the variable consistent with the database
    // version of the language and to prevent checking against an outdated hash.
    $default_langcode = language_default('language');
    if ($default_langcode == $language->language) {
      $default = db_query("SELECT * FROM {languages} WHERE language = :language", array(':language' => $default_langcode))->fetchObject();
      variable_set('language_default', $default);
    }
  }

  // Log the operation and return success flag.
  switch ($status) {
    case 'updated':
      watchdog('locale', 'Updated JavaScript translation file for the language %language.', array('%language' => t($language->name)));
      return TRUE;
    case 'rebuilt':
      watchdog('locale', 'JavaScript translation file %file.js was lost.', array('%file' => $language->javascript), WATCHDOG_WARNING);
      // Proceed to the 'created' case as the JavaScript translation file has
      // been created again.
    case 'created':
      watchdog('locale', 'Created JavaScript translation file for the language %language.', array('%language' => t($language->name)));
      return TRUE;
    case 'deleted':
      watchdog('locale', 'Removed JavaScript translation file for the language %language, because no translations currently exist for that language.', array('%language' => t($language->name)));
      return TRUE;
    case 'error':
      watchdog('locale', 'An error occurred during creation of the JavaScript translation file for the language %language.', array('%language' => t($language->name)), WATCHDOG_ERROR);
      return FALSE;
    default:
      // No operation needed.
      return TRUE;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
