# list_themes()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 774–826 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L774-L826)

## Signature

```php
function list_themes($refresh = FALSE)
```

## Documentation

```text
Returns a list of all currently available themes.

Retrieved from the database, if available and the site is not in maintenance
mode; otherwise compiled freshly from the filesystem.

@param $refresh
  Whether to reload the list of themes from the database. Defaults to FALSE.

@return
  An associative array of the currently available themes. The keys are the
  themes' machine names and the values are objects having the following
  properties:
  - filename: The filepath and name of the .info file.
  - name: The machine name of the theme.
  - status: 1 for enabled, 0 for disabled themes.
  - info: The contents of the .info file.
  - stylesheets: A two dimensional array, using the first key for the
    media attribute (e.g. 'all'), the second for the name of the file
    (e.g. style.css). The value is a complete filepath (e.g.
    themes/bartik/style.css). Not set if no stylesheets are defined in the
    .info file.
  - scripts: An associative array of JavaScripts, using the filename as key
    and the complete filepath as value. Not set if no scripts are defined in
    the .info file.
  - prefix: The base theme engine prefix.
  - engine: The machine name of the theme engine.
  - base_theme: If this is a sub-theme, the machine name of the base theme
    defined in the .info file. Otherwise, the element is not set.
  - base_themes: If this is a sub-theme, an associative array of the
    base-theme ancestors of this theme, starting with this theme's base
    theme, then the base theme's own base theme, etc. Each entry has an
    array key equal to the theme's machine name, and a value equal to the
    human-readable theme name; if a theme with matching machine name does
    not exist in the system, the value will instead be NULL (and since the
    system would not know whether that theme itself has a base theme, that
    will end the array of base themes). This is not set if the theme is not
    a sub-theme.
  - sub_themes: An associative array of themes on the system that are
    either direct sub-themes (that is, they declare this theme to be
    their base theme), direct sub-themes of sub-themes, etc. The keys are
    the themes' machine names, and the values are the themes' human-readable
    names. This element is not set if there are no themes on the system that
    declare this theme as their base theme.
```

## Code

```php
function list_themes($refresh = FALSE) {
  $list = &drupal_static(__FUNCTION__, array());

  if ($refresh) {
    $list = array();
    system_list_reset();
  }

  if (empty($list)) {
    $list = array();
    $themes = array();
    // Extract from the database only when it is available.
    // Also check that the site is not in the middle of an install or update.
    if (!defined('MAINTENANCE_MODE')) {
      try {
        $themes = system_list('theme');
      }
      catch (Exception $e) {
        // If the database is not available, rebuild the theme data.
        $themes = _system_rebuild_theme_data();
      }
    }
    else {
      // Scan the installation when the database should not be read.
      $themes = _system_rebuild_theme_data();
    }

    foreach ($themes as $theme) {
      foreach ($theme->info['stylesheets'] as $media => $stylesheets) {
        foreach ($stylesheets as $stylesheet => $path) {
          $theme->stylesheets[$media][$stylesheet] = $path;
        }
      }
      foreach ($theme->info['scripts'] as $script => $path) {
        $theme->scripts[$script] = $path;
      }
      if (isset($theme->info['engine'])) {
        $theme->engine = $theme->info['engine'];
      }
      if (isset($theme->info['base theme'])) {
        $theme->base_theme = $theme->info['base theme'];
      }
      // Status is normally retrieved from the database. Add zero values when
      // read from the installation directory to prevent notices.
      if (!isset($theme->status)) {
        $theme->status = 0;
      }
      $list[$theme->name] = $theme;
    }
  }

  return $list;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
