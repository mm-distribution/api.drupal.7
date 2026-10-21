# _theme_process_registry()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 515–665 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L515-L665)

## Signature

```php
function _theme_process_registry(&$cache, $name, $type, $theme, $path)
```

## Documentation

```text
Process a single implementation of hook_theme().

@param $cache
  The theme registry that will eventually be cached; It is an associative
  array keyed by theme hooks, whose values are associative arrays describing
  the hook:
  - 'type': The passed-in $type.
  - 'theme path': The passed-in $path.
  - 'function': The name of the function generating output for this theme
    hook. Either defined explicitly in hook_theme() or, if neither 'function'
    nor 'template' is defined, then the default theme function name is used.
    The default theme function name is the theme hook prefixed by either
    'theme_' for modules or '$name_' for everything else. If 'function' is
    defined, 'template' is not used.
  - 'template': The filename of the template generating output for this
    theme hook. The template is in the directory defined by the 'path' key of
    hook_theme() or defaults to $path.
  - 'variables': The variables for this theme hook as defined in
    hook_theme(). If there is more than one implementation and 'variables' is
    not specified in a later one, then the previous definition is kept.
  - 'render element': The renderable element for this theme hook as defined
    in hook_theme(). If there is more than one implementation and
    'render element' is not specified in a later one, then the previous
    definition is kept.
  - 'preprocess functions': See theme() for detailed documentation.
  - 'process functions': See theme() for detailed documentation.
@param $name
  The name of the module, theme engine, base theme engine, theme or base
  theme implementing hook_theme().
@param $type
  One of 'module', 'theme_engine', 'base_theme_engine', 'theme', or
  'base_theme'. Unlike regular hooks that can only be implemented by modules,
  each of these can implement hook_theme(). _theme_process_registry() is
  called in aforementioned order and new entries override older ones. For
  example, if a theme hook is both defined by a module and a theme, then the
  definition in the theme will be used.
@param $theme
  The loaded $theme object as returned from list_themes().
@param $path
  The directory where $name is. For example, modules/system or
  themes/bartik.

@see theme()
@see _theme_build_registry()
@see hook_theme()
@see list_themes()
```

## Code

```php
function _theme_process_registry(&$cache, $name, $type, $theme, $path) {
  $result = array();

  // Processor functions work in two distinct phases with the process
  // functions always being executed after the preprocess functions.
  $variable_process_phases = array(
    'preprocess functions' => 'preprocess',
    'process functions'    => 'process',
  );

  $hook_defaults = array(
    'variables' => TRUE,
    'render element' => TRUE,
    'pattern' => TRUE,
    'base hook' => TRUE,
  );

  // Invoke the hook_theme() implementation, process what is returned, and
  // merge it into $cache.
  $function = $name . '_theme';
  if (function_exists($function)) {
    $result = $function($cache, $type, $theme, $path);
    foreach ($result as $hook => $info) {
      // When a theme or engine overrides a module's theme function
      // $result[$hook] will only contain key/value pairs for information being
      // overridden.  Pull the rest of the information from what was defined by
      // an earlier hook.

      // Fill in the type and path of the module, theme, or engine that
      // implements this theme function.
      $result[$hook]['type'] = $type;
      $result[$hook]['theme path'] = $path;

      // If function and file are omitted, default to standard naming
      // conventions.
      if (!isset($info['template']) && !isset($info['function'])) {
        $result[$hook]['function'] = ($type == 'module' ? 'theme_' : $name . '_') . $hook;
      }

      if (isset($cache[$hook]['includes'])) {
        $result[$hook]['includes'] = $cache[$hook]['includes'];
      }

      // If the theme implementation defines a file, then also use the path
      // that it defined. Otherwise use the default path. This allows
      // system.module to declare theme functions on behalf of core .include
      // files.
      if (isset($info['file'])) {
        $include_file = isset($info['path']) ? $info['path'] : $path;
        $include_file .= '/' . $info['file'];
        include_once DRUPAL_ROOT . '/' . $include_file;
        $result[$hook]['includes'][] = $include_file;
      }

      // If the default keys are not set, use the default values registered
      // by the module.
      if (isset($cache[$hook])) {
        $result[$hook] += array_intersect_key($cache[$hook], $hook_defaults);
      }

      // The following apply only to theming hooks implemented as templates.
      if (isset($info['template'])) {
        // Prepend the current theming path when none is set.
        if (!isset($info['path'])) {
          $result[$hook]['template'] = $path . '/' . $info['template'];
        }
      }

      // Allow variable processors for all theming hooks, whether the hook is
      // implemented as a template or as a function.
      foreach ($variable_process_phases as $phase_key => $phase) {
        // Check for existing variable processors. Ensure arrayness.
        if (!isset($info[$phase_key]) || !is_array($info[$phase_key])) {
          $info[$phase_key] = array();
          $prefixes = array();
          if ($type == 'module') {
            // Default variable processor prefix.
            $prefixes[] = 'template';
            // Add all modules so they can intervene with their own variable
            // processors. This allows them to provide variable processors even
            // if they are not the owner of the current hook.
            $prefixes += module_list();
          }
          elseif ($type == 'theme_engine' || $type == 'base_theme_engine') {
            // Theme engines get an extra set that come before the normally
            // named variable processors.
            $prefixes[] = $name . '_engine';
            // The theme engine registers on behalf of the theme using the
            // theme's name.
            $prefixes[] = $theme;
          }
          else {
            // This applies when the theme manually registers their own variable
            // processors.
            $prefixes[] = $name;
          }
          foreach ($prefixes as $prefix) {
            // Only use non-hook-specific variable processors for theming hooks
            // implemented as templates. See theme().
            if (isset($info['template']) && function_exists($prefix . '_' . $phase)) {
              $info[$phase_key][] = $prefix . '_' . $phase;
            }
            if (function_exists($prefix . '_' . $phase . '_' . $hook)) {
              $info[$phase_key][] = $prefix . '_' . $phase . '_' . $hook;
            }
          }
        }
        // Check for the override flag and prevent the cached variable
        // processors from being used. This allows themes or theme engines to
        // remove variable processors set earlier in the registry build.
        if (!empty($info['override ' . $phase_key])) {
          // Flag not needed inside the registry.
          unset($result[$hook]['override ' . $phase_key]);
        }
        elseif (isset($cache[$hook][$phase_key]) && is_array($cache[$hook][$phase_key])) {
          $info[$phase_key] = array_merge($cache[$hook][$phase_key], $info[$phase_key]);
        }
        $result[$hook][$phase_key] = $info[$phase_key];
      }
    }

    // Merge the newly created theme hooks into the existing cache.
    $cache = $result + $cache;
  }

  // Let themes have variable processors even if they didn't register a
  // template.
  if ($type == 'theme' || $type == 'base_theme') {
    foreach ($cache as $hook => $info) {
      // Check only if not registered by the theme or engine.
      if (empty($result[$hook])) {
        foreach ($variable_process_phases as $phase_key => $phase) {
          if (!isset($info[$phase_key])) {
            $cache[$hook][$phase_key] = array();
          }
          // Only use non-hook-specific variable processors for theming hooks
          // implemented as templates. See theme().
          if (isset($info['template']) && function_exists($name . '_' . $phase)) {
            $cache[$hook][$phase_key][] = $name . '_' . $phase;
          }
          if (function_exists($name . '_' . $phase . '_' . $hook)) {
            $cache[$hook][$phase_key][] = $name . '_' . $phase . '_' . $hook;
            $cache[$hook]['theme path'] = $path;
          }
          // Ensure uniqueness.
          $cache[$hook][$phase_key] = array_unique($cache[$hook][$phase_key]);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
