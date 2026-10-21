# _system_rebuild_theme_data()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2532–2658 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2532-L2658)
- **Module/theme:** system

## Signature

```php
function _system_rebuild_theme_data()
```

## Documentation

```text
Helper function to scan and collect theme .info data and their engines.

@return
  An associative array of themes information.
```

## Code

```php
function _system_rebuild_theme_data() {
  // Find themes
  $themes = drupal_system_listing('/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.info$/', 'themes');
  // Allow modules to add further themes.
  if ($module_themes = module_invoke_all('system_theme_info')) {
    foreach ($module_themes as $name => $uri) {
      // @see file_scan_directory()
      $themes[$name] = (object) array(
        'uri' => $uri,
        'filename' => pathinfo($uri, PATHINFO_FILENAME),
        'name' => $name,
      );
    }
  }

  // Find theme engines
  $engines = drupal_system_listing('/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.engine$/', 'themes/engines');
  // Allow modules to add further theme engines.
  if ($module_engines = module_invoke_all('system_theme_engine_info')) {
    foreach ($module_engines as $name => $theme_engine_path) {
      $engines[$name] = (object) array(
        'uri' => $theme_engine_path,
        'filename' => basename($theme_engine_path),
        'name' => $name,
      );
    }
  }

  // Set defaults for theme info.
  $defaults = array(
    'engine' => 'phptemplate',
    'regions' => array(
      'sidebar_first' => 'Left sidebar',
      'sidebar_second' => 'Right sidebar',
      'content' => 'Content',
      'header' => 'Header',
      'footer' => 'Footer',
      'highlighted' => 'Highlighted',
      'help' => 'Help',
      'page_top' => 'Page top',
      'page_bottom' => 'Page bottom',
    ),
    'description' => '',
    'features' => _system_default_theme_features(),
    'screenshot' => 'screenshot.png',
    'php' => DRUPAL_MINIMUM_PHP,
    'stylesheets' => array(),
    'scripts' => array(),
  );

  $sub_themes = array();
  // Read info files for each theme
  foreach ($themes as $key => $theme) {
    $themes[$key]->filename = $theme->uri;
    $themes[$key]->info = drupal_parse_info_file($theme->uri) + $defaults;

    // The "name" key is required, but to avoid a fatal error in the menu system
    // we set a reasonable default if it is not provided.
    $themes[$key]->info += array('name' => $key);

    // Add the info file modification time, so it becomes available for
    // contributed modules to use for ordering theme lists.
    $themes[$key]->info['mtime'] = filemtime($theme->uri);

    // Invoke hook_system_info_alter() to give installed modules a chance to
    // modify the data in the .info files if necessary.
    $type = 'theme';
    drupal_alter('system_info', $themes[$key]->info, $themes[$key], $type);

    if (!empty($themes[$key]->info['base theme'])) {
      $sub_themes[] = $key;
    }
    if ($themes[$key]->info['engine'] == 'theme') {
      $filename = dirname($themes[$key]->uri) . '/' . $themes[$key]->name . '.theme';
      if (file_exists($filename)) {
        $themes[$key]->owner = $filename;
        $themes[$key]->prefix = $key;
      }
    }
    else {
      $engine = $themes[$key]->info['engine'];
      if (isset($engines[$engine])) {
        $themes[$key]->owner = $engines[$engine]->uri;
        $themes[$key]->prefix = $engines[$engine]->name;
        $themes[$key]->template = TRUE;
      }
    }

    // Prefix stylesheets and scripts with module path.
    $path = dirname($theme->uri);
    $theme->info['stylesheets'] = _system_info_add_path($theme->info['stylesheets'], $path);
    $theme->info['scripts'] = _system_info_add_path($theme->info['scripts'], $path);

    // Give the screenshot proper path information.
    if (!empty($themes[$key]->info['screenshot'])) {
      $themes[$key]->info['screenshot'] = $path . '/' . $themes[$key]->info['screenshot'];
    }
  }

  // Now that we've established all our master themes, go back and fill in data
  // for subthemes.
  foreach ($sub_themes as $key) {
    $themes[$key]->base_themes = drupal_find_base_themes($themes, $key);
    // Don't proceed if there was a problem with the root base theme.
    if (!current($themes[$key]->base_themes)) {
      continue;
    }
    $base_key = key($themes[$key]->base_themes);
    foreach (array_keys($themes[$key]->base_themes) as $base_theme) {
      $themes[$base_theme]->sub_themes[$key] = $themes[$key]->info['name'];
    }
    // Copy the 'owner' and 'engine' over if the top level theme uses a theme
    // engine.
    if (isset($themes[$base_key]->owner)) {
      if (isset($themes[$base_key]->info['engine'])) {
        $themes[$key]->info['engine'] = $themes[$base_key]->info['engine'];
        $themes[$key]->owner = $themes[$base_key]->owner;
        $themes[$key]->prefix = $themes[$base_key]->prefix;
      }
      else {
        $themes[$key]->prefix = $key;
      }
    }
  }

  return $themes;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
