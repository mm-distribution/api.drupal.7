# overlay_overlay_parent_initialize()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 671–694 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L671-L694)
- **Module/theme:** overlay
- **Implements:** [hook_overlay_parent_initialize()](../overlay.api.php/hook_overlay_parent_initialize.md)

## Signature

```php
function overlay_overlay_parent_initialize()
```

## Documentation

```text
Implements hook_overlay_parent_initialize().
```

## Code

```php
function overlay_overlay_parent_initialize() {
  // Let the client side know which paths are administrative.
  $paths = path_get_admin_paths();
  foreach ($paths as &$type) {
    $type = str_replace('<front>', variable_get('site_frontpage', 'node'), $type);
  }
  drupal_add_js(array('overlay' => array('paths' => $paths)), 'setting');
  $path_prefixes = array();
  if (module_exists('locale') && variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX) == LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX) {
    // Get languages grouped by status and select only the enabled ones.
    $languages = language_list('enabled');
    $languages = $languages[1];

    $path_prefixes = array();
    foreach ($languages as $language) {
      if ($language->prefix) {
        $path_prefixes[] = $language->prefix;
      }
    }
  }
  drupal_add_js(array('overlay' => array('pathPrefixes' => $path_prefixes)), 'setting');
  // Pass along the Ajax callback for rerendering sections of the parent window.
  drupal_add_js(array('overlay' => array('ajaxCallback' => 'overlay-ajax')), 'setting');
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
