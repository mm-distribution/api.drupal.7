# locale_js_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 903–957 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L903-L957)
- **Module/theme:** locale
- **Implements:** [hook_js_alter()](../../system/system.api.php/hook_js_alter.md)

## Signature

```php
function locale_js_alter(&$javascript)
```

## Documentation

```text
Implements hook_js_alter().

This function checks all JavaScript files currently added via drupal_add_js()
and invokes parsing if they have not yet been parsed for Drupal.t()
and Drupal.formatPlural() calls. Also refreshes the JavaScript translation
file if necessary, and adds it to the page.
```

## Code

```php
function locale_js_alter(&$javascript) {
  global $language;

  $dir = 'public://' . variable_get('locale_js_directory', 'languages');
  $parsed = variable_get('javascript_parsed', array());
  $files = $new_files = FALSE;

  // Require because locale_js_alter() could be called without locale_init().
  require_once DRUPAL_ROOT . '/includes/locale.inc';

  foreach ($javascript as $item) {
    if ($item['type'] == 'file') {
      $files = TRUE;
      $filepath = $item['data'];
      if (!in_array($filepath, $parsed)) {
        // Don't parse our own translations files.
        if (substr($filepath, 0, strlen($dir)) != $dir) {
          _locale_parse_js_file($filepath);
          $parsed[] = $filepath;
          $new_files = TRUE;
        }
      }
    }
  }

  // If there are any new source files we parsed, invalidate existing
  // JavaScript translation files for all languages, adding the refresh
  // flags into the existing array.
  if ($new_files) {
    $parsed += _locale_invalidate_js();
  }

  // If necessary, rebuild the translation file for the current language.
  if (!empty($parsed['refresh:' . $language->language])) {
    // Don't clear the refresh flag on failure, so that another try will
    // be performed later.
    if (_locale_rebuild_js()) {
      unset($parsed['refresh:' . $language->language]);
    }
    // Store any changes after refresh was attempted.
    variable_set('javascript_parsed', $parsed);
  }
  // If no refresh was attempted, but we have new source files, we need
  // to store them too. This occurs if current page is in English.
  elseif ($new_files) {
    variable_set('javascript_parsed', $parsed);
  }

  // Add the translation JavaScript file to the page.
  if ($files && !empty($language->javascript)) {
    // Add the translation JavaScript file to the page.
    $file = $dir . '/' . $language->language . '_' . $language->javascript . '.js';
    $javascript[$file] = drupal_js_defaults($file);
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
