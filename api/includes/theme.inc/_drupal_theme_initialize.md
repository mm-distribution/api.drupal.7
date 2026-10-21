# _drupal_theme_initialize()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 141–236 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L141-L236)

## Signature

```php
function _drupal_theme_initialize($theme, $base_theme = array(), $registry_callback = '_theme_load_registry')
```

## Documentation

```text
Initializes the theme system given already loaded information.

This function is useful to initialize a theme when no database is present.

@param $theme
  An object with the following information:
    filename
      The .info file for this theme. The 'path' to
      the theme will be in this file's directory. (Required)
    owner
      The path to the .theme file or the .engine file to load for
      the theme. (Required)
    stylesheet
      The primary stylesheet for the theme. (Optional)
    engine
      The name of theme engine to use. (Optional)
@param $base_theme
   An optional array of objects that represent the 'base theme' if the
   theme is meant to be derivative of another theme. It requires
   the same information as the $theme object. It should be in
   'oldest first' order, meaning the top level of the chain will
   be first.
@param $registry_callback
  The callback to invoke to set the theme registry.
```

## Code

```php
function _drupal_theme_initialize($theme, $base_theme = array(), $registry_callback = '_theme_load_registry') {
  global $theme_info, $base_theme_info, $theme_engine, $theme_path;
  $theme_info = $theme;
  $base_theme_info = $base_theme;

  $theme_path = dirname($theme->filename);

  // Prepare stylesheets from this theme as well as all ancestor themes.
  // We work it this way so that we can have child themes override parent
  // theme stylesheets easily.
  $final_stylesheets = array();

  // Grab stylesheets from base theme
  foreach ($base_theme as $base) {
    if (!empty($base->stylesheets)) {
      foreach ($base->stylesheets as $media => $stylesheets) {
        foreach ($stylesheets as $name => $stylesheet) {
          $final_stylesheets[$media][$name] = $stylesheet;
        }
      }
    }
  }

  // Add stylesheets used by this theme.
  if (!empty($theme->stylesheets)) {
    foreach ($theme->stylesheets as $media => $stylesheets) {
      foreach ($stylesheets as $name => $stylesheet) {
        $final_stylesheets[$media][$name] = $stylesheet;
      }
    }
  }

  // And now add the stylesheets properly
  foreach ($final_stylesheets as $media => $stylesheets) {
    foreach ($stylesheets as $stylesheet) {
      drupal_add_css($stylesheet, array('group' => CSS_THEME, 'every_page' => TRUE, 'media' => $media));
    }
  }

  // Do basically the same as the above for scripts
  $final_scripts = array();

  // Grab scripts from base theme
  foreach ($base_theme as $base) {
    if (!empty($base->scripts)) {
      foreach ($base->scripts as $name => $script) {
        $final_scripts[$name] = $script;
      }
    }
  }

  // Add scripts used by this theme.
  if (!empty($theme->scripts)) {
    foreach ($theme->scripts as $name => $script) {
      $final_scripts[$name] = $script;
    }
  }

  // Add scripts used by this theme.
  foreach ($final_scripts as $script) {
    drupal_add_js($script, array('group' => JS_THEME, 'every_page' => TRUE));
  }

  $theme_engine = NULL;

  // Initialize the theme.
  if (isset($theme->engine)) {
    // Include the engine.
    include_once DRUPAL_ROOT . '/' . $theme->owner;

    $theme_engine = $theme->engine;
    if (function_exists($theme_engine . '_init')) {
      foreach ($base_theme as $base) {
        call_user_func($theme_engine . '_init', $base);
      }
      call_user_func($theme_engine . '_init', $theme);
    }
  }
  else {
    // include non-engine theme files
    foreach ($base_theme as $base) {
      // Include the theme file or the engine.
      if (!empty($base->owner)) {
        include_once DRUPAL_ROOT . '/' . $base->owner;
      }
    }
    // and our theme gets one too.
    if (!empty($theme->owner)) {
      include_once DRUPAL_ROOT . '/' . $theme->owner;
    }
  }

  if (isset($registry_callback)) {
    _theme_registry_callback($registry_callback, array($theme, $base_theme, $theme_engine));
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
