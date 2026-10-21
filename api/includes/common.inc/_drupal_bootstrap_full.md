# _drupal_bootstrap_full()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5385–5450 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5385-L5450)

## Signature

```php
function _drupal_bootstrap_full()
```

## Documentation

_No docblock in source._

## Code

```php
function _drupal_bootstrap_full() {
  static $called = FALSE;

  if ($called) {
    return;
  }
  $called = TRUE;
  require_once DRUPAL_ROOT . '/' . variable_get('path_inc', 'includes/path.inc');
  require_once DRUPAL_ROOT . '/includes/theme.inc';
  require_once DRUPAL_ROOT . '/includes/pager.inc';
  require_once DRUPAL_ROOT . '/' . variable_get('menu_inc', 'includes/menu.inc');
  require_once DRUPAL_ROOT . '/includes/tablesort.inc';
  require_once DRUPAL_ROOT . '/includes/file.inc';
  require_once DRUPAL_ROOT . '/includes/unicode.inc';
  require_once DRUPAL_ROOT . '/includes/image.inc';
  require_once DRUPAL_ROOT . '/includes/form.inc';
  require_once DRUPAL_ROOT . '/includes/mail.inc';
  require_once DRUPAL_ROOT . '/includes/actions.inc';
  require_once DRUPAL_ROOT . '/includes/ajax.inc';
  require_once DRUPAL_ROOT . '/includes/token.inc';
  require_once DRUPAL_ROOT . '/includes/errors.inc';

  // Detect string handling method
  unicode_check();
  // Undo magic quotes
  fix_gpc_magic();
  // Load all enabled modules
  module_load_all();
  // Reset drupal_alter() and module_implements() static caches as these
  // include implementations for vital modules only when called early on
  // in the bootstrap.
  drupal_static_reset('drupal_alter');
  drupal_static_reset('module_implements');
  // Make sure all stream wrappers are registered.
  file_get_stream_wrappers();
  // Ensure mt_rand is reseeded, to prevent random values from one page load
  // being exploited to predict random values in subsequent page loads.
  $seed = unpack("L", drupal_random_bytes(4));
  mt_srand($seed[1]);

  $test_info = &$GLOBALS['drupal_test_info'];
  if (!empty($test_info['in_child_site'])) {
    // Running inside the simpletest child site, log fatal errors to test
    // specific file directory.
    ini_set('log_errors', 1);
    ini_set('error_log', 'public://error.log');
  }

  // Initialize $_GET['q'] prior to invoking hook_init().
  drupal_path_initialize();

  // Let all modules take action before the menu system handles the request.
  // We do not want this while running update.php.
  if (!defined('MAINTENANCE_MODE') || MAINTENANCE_MODE != 'update') {
    // Prior to invoking hook_init(), initialize the theme (potentially a custom
    // one for this page), so that:
    // - Modules with hook_init() implementations that call theme() or
    //   theme_get_registry() don't initialize the incorrect theme.
    // - The theme can have hook_*_alter() implementations affect page building
    //   (e.g., hook_form_alter(), hook_node_view_alter(), hook_page_alter()),
    //   ahead of when rendering starts.
    menu_set_custom_theme();
    drupal_theme_initialize();
    module_invoke_all('init');
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
