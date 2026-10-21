# locale_add_language()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 595–641 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L595-L641)
- **Topics:** [locale-api-add](../../topics/locale-api-add.md)

## Signature

```php
function locale_add_language($langcode, $name = NULL, $native = NULL, $direction = LANGUAGE_LTR, $domain = '', $prefix = '', $enabled = TRUE, $default = FALSE)
```

## Documentation

```text
API function to add a language.

@param $langcode
  Language code.
@param $name
  English name of the language
@param $native
  Native name of the language
@param $direction
  LANGUAGE_LTR or LANGUAGE_RTL
@param $domain
  Optional custom domain name with protocol, without
  trailing slash (eg. http://de.example.com).
@param $prefix
  Optional path prefix for the language. Defaults to the
  language code if omitted.
@param $enabled
  Optionally TRUE to enable the language when created or FALSE to disable.
@param $default
  Optionally set this language to be the default.
```

## Code

```php
function locale_add_language($langcode, $name = NULL, $native = NULL, $direction = LANGUAGE_LTR, $domain = '', $prefix = '', $enabled = TRUE, $default = FALSE) {
  // Default prefix on language code.
  if (empty($prefix)) {
    $prefix = $langcode;
  }

  // If name was not set, we add a predefined language.
  if (!isset($name)) {
    include_once DRUPAL_ROOT . '/includes/iso.inc';
    $predefined = _locale_get_predefined_list();
    $name = $predefined[$langcode][0];
    $native = isset($predefined[$langcode][1]) ? $predefined[$langcode][1] : $predefined[$langcode][0];
    $direction = isset($predefined[$langcode][2]) ? $predefined[$langcode][2] : LANGUAGE_LTR;
  }

  db_insert('languages')
    ->fields(array(
      'language' => $langcode,
      'name' => $name,
      'native' => $native,
      'direction' => $direction,
      'domain' => $domain,
      'prefix' => $prefix,
      'enabled' => $enabled ? 1 : 0,
    ))
    ->execute();

  // Only set it as default if enabled.
  if ($enabled && $default) {
    variable_set('language_default', (object) array('language' => $langcode, 'name' => $name, 'native' => $native, 'direction' => $direction, 'enabled' => (int) $enabled, 'plurals' => 0, 'formula' => '', 'domain' => '', 'prefix' => $prefix, 'weight' => 0, 'javascript' => ''));
  }

  if ($enabled) {
    // Increment enabled language count if we are adding an enabled language.
    variable_set('language_count', variable_get('language_count', 1) + 1);
  }

  // Kill the static cache in language_list().
  drupal_static_reset('language_list');

  // Force JavaScript translation file creation for the newly added language.
  _locale_invalidate_js($langcode);

  watchdog('locale', 'The %language language (%code) has been created.', array('%language' => $name, '%code' => $langcode));

  module_invoke_all('multilingual_settings_changed');
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
