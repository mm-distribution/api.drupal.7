# _drupal_maintenance_theme()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 17–85 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L17-L85)

## Signature

```php
function _drupal_maintenance_theme()
```

## Documentation

```text
Sets up the theming system for maintenance page.

Used for site installs, updates and when the site is in maintenance mode.
It also applies when the database is unavailable or bootstrap was not
complete. Seven is always used for the initial install and update
operations. In other cases, Bartik is used, but this can be overridden by
setting a "maintenance_theme" key in the $conf variable in settings.php.
```

## Code

```php
function _drupal_maintenance_theme() {
  global $theme, $theme_key, $conf;

  // If $theme is already set, assume the others are set too, and do nothing.
  if (isset($theme)) {
    return;
  }

  require_once DRUPAL_ROOT . '/' . variable_get('path_inc', 'includes/path.inc');
  require_once DRUPAL_ROOT . '/includes/theme.inc';
  require_once DRUPAL_ROOT . '/includes/common.inc';
  require_once DRUPAL_ROOT . '/includes/unicode.inc';
  require_once DRUPAL_ROOT . '/includes/file.inc';
  require_once DRUPAL_ROOT . '/includes/module.inc';
  unicode_check();

  // Install and update pages are treated differently to prevent theming overrides.
  if (defined('MAINTENANCE_MODE') && (MAINTENANCE_MODE == 'install' || MAINTENANCE_MODE == 'update')) {
    $custom_theme = (isset($conf['maintenance_theme']) ? $conf['maintenance_theme'] : 'seven');
  }
  else {
    // The bootstrap was not complete. So we are operating in a crippled
    // environment, we need to bootstrap just enough to allow hook invocations
    // to work. See _drupal_log_error().
    if (!class_exists('Database', FALSE)) {
      require_once DRUPAL_ROOT . '/includes/database/database.inc';
    }

    // We use the default theme as the maintenance theme. If a default theme
    // isn't specified in the database or in settings.php, we use Bartik.
    $custom_theme = variable_get('maintenance_theme', variable_get('theme_default', 'bartik'));
  }

  // Ensure that system.module is loaded.
  if (!function_exists('_system_rebuild_theme_data')) {
    $module_list['system']['filename'] = 'modules/system/system.module';
    module_list(TRUE, FALSE, FALSE, $module_list);
    drupal_load('module', 'system');
  }

  $themes = list_themes();

  // list_themes() triggers a drupal_alter() in maintenance mode, but we can't
  // let themes alter the .info data until we know a theme's base themes. So
  // don't set global $theme until after list_themes() builds its cache.
  $theme = $custom_theme;

  // Store the identifier for retrieving theme settings with.
  $theme_key = $theme;

  // Find all our ancestor themes and put them in an array.
  $base_theme = array();
  $ancestor = $theme;
  while ($ancestor && isset($themes[$ancestor]->base_theme)) {
    $base_theme[] = $new_base_theme = $themes[$themes[$ancestor]->base_theme];
    $ancestor = $themes[$ancestor]->base_theme;
  }
  _drupal_theme_initialize($themes[$theme], array_reverse($base_theme), '_theme_load_offline_registry');

  // These are usually added from system_init() -except maintenance.css.
  // When the database is inactive it's not called so we add it here.
  $path = drupal_get_path('module', 'system');
  drupal_add_css($path . '/system.base.css');
  drupal_add_css($path . '/system.admin.css');
  drupal_add_css($path . '/system.menus.css');
  drupal_add_css($path . '/system.messages.css');
  drupal_add_css($path . '/system.theme.css');
  drupal_add_css($path . '/system.maintenance.css');
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
