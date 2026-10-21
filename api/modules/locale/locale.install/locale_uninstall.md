# locale_uninstall()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 224–269 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L224-L269)
- **Module/theme:** locale
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function locale_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function locale_uninstall() {
  // Delete all JavaScript translation files.
  $locale_js_directory = 'public://' . variable_get('locale_js_directory', 'languages');

  if (is_dir($locale_js_directory)) {
    $files = db_query('SELECT language, javascript FROM {languages}');
    foreach ($files as $file) {
      if (!empty($file->javascript)) {
        file_unmanaged_delete($locale_js_directory . '/' . $file->language . '_' . $file->javascript . '.js');
      }
    }
    // Delete the JavaScript translations directory if empty.
    if (!file_scan_directory($locale_js_directory, '/.*/')) {
      drupal_rmdir($locale_js_directory);
    }
  }

  // Clear variables.
  variable_del('language_default');
  variable_del('language_count');
  variable_del('language_types');
  variable_del('locale_language_negotiation_url_part');
  variable_del('locale_language_negotiation_session_param');
  variable_del('language_content_type_default');
  variable_del('language_content_type_negotiation');
  variable_del('locale_cache_strings');
  variable_del('locale_js_directory');
  variable_del('javascript_parsed');
  variable_del('locale_field_language_fallback');
  variable_del('locale_cache_length');

  foreach (language_types() as $type) {
    variable_del("language_negotiation_$type");
    variable_del("locale_language_providers_weight_$type");
  }

  foreach (node_type_get_types() as $type => $content_type) {
    $setting = variable_del("language_content_type_$type");
  }

  // Switch back to English: with a $language->language value different from 'en'
  // successive calls of t() might result in calling locale(), which in turn might
  // try to query the unexisting {locales_source} and {locales_target} tables.
  drupal_language_initialize();

}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
