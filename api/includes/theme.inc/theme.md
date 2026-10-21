# theme()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1012–1215 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1012-L1215)

## Signature

```php
function theme($hook, $variables = array())
```

## Documentation

```text
Generates themed output.

All requests for themed output must go through this function (however,
calling the theme() function directly is strongly discouraged - see next
paragraph). It examines the request and routes it to the appropriate
@link themeable theme function or template @endlink, by checking the theme
registry.

Avoid calling this function directly. It is preferable to replace direct
calls to the theme() function with calls to drupal_render() by passing a
render array with a #theme key to drupal_render(), which in turn calls
theme().

@section sec_theme_hooks Theme Hooks
Most commonly, the first argument to this function is the name of the theme
hook. For instance, to theme a taxonomy term, the theme hook name is
'taxonomy_term'. Modules register theme hooks within a hook_theme()
implementation and provide a default implementation via a function named
theme_HOOK() (e.g., theme_taxonomy_term()) or via a template file named
according to the value of the 'template' key registered with the theme hook
(see hook_theme() for details). Default templates are implemented with the
PHPTemplate rendering engine and are named the same as the theme hook, with
underscores changed to hyphens, so for the 'taxonomy_term' theme hook, the
default template is 'taxonomy-term.tpl.php'.

@subsection sub_overriding_theme_hooks Overriding Theme Hooks
Themes may also register new theme hooks within a hook_theme()
implementation, but it is more common for themes to override default
implementations provided by modules than to register entirely new theme
hooks. Themes can override a default implementation by implementing a
function named THEME_HOOK() (for example, the 'bartik' theme overrides the
default implementation of the 'menu_tree' theme hook by implementing a
bartik_menu_tree() function), or by adding a template file within its folder
structure that follows the template naming structure used by the theme's
rendering engine (for example, since the Bartik theme uses the PHPTemplate
rendering engine, it overrides the default implementation of the 'page' theme
hook by containing a 'page.tpl.php' file within its folder structure).

@subsection sub_preprocess_templates Preprocessing for Template Files
If the implementation is a template file, several functions are called
before the template file is invoked, to modify the $variables array. These
fall into the "preprocessing" phase and the "processing" phase, and are
executed (if they exist), in the following order (note that in the following
list, HOOK indicates the theme hook name, MODULE indicates a module name,
THEME indicates a theme name, and ENGINE indicates a theme engine name):
- template_preprocess(&$variables, $hook): Creates a default set of
  variables for all theme hooks with template implementations.
- template_preprocess_HOOK(&$variables): Should be implemented by the module
  that registers the theme hook, to set up default variables.
- MODULE_preprocess(&$variables, $hook): hook_preprocess() is invoked on all
  implementing modules.
- MODULE_preprocess_HOOK(&$variables): hook_preprocess_HOOK() is invoked on
  all implementing modules, so that modules that didn't define the theme
  hook can alter the variables.
- ENGINE_engine_preprocess(&$variables, $hook): Allows the theme engine to
  set necessary variables for all theme hooks with template implementations.
- ENGINE_engine_preprocess_HOOK(&$variables): Allows the theme engine to set
  necessary variables for the particular theme hook.
- THEME_preprocess(&$variables, $hook): Allows the theme to set necessary
  variables for all theme hooks with template implementations.
- THEME_preprocess_HOOK(&$variables): Allows the theme to set necessary
  variables specific to the particular theme hook.
- template_process(&$variables, $hook): Creates an additional set of default
  variables for all theme hooks with template implementations. The variables
  created in this function are derived from ones created by
  template_preprocess(), but potentially altered by the other preprocess
  functions listed above. For example, any preprocess function can add to or
  modify the $variables['attributes_array'] variable, and after all of them
  have finished executing, template_process() flattens it into a
  $variables['attributes'] string for convenient use by templates.
- template_process_HOOK(&$variables): Should be implemented by the module
  that registers the theme hook, if it needs to perform additional variable
  processing after all preprocess functions have finished.
- MODULE_process(&$variables, $hook): hook_process() is invoked on all
  implementing modules.
- MODULE_process_HOOK(&$variables): hook_process_HOOK() is invoked on
  on all implementing modules, so that modules that didn't define the theme
  hook can alter the variables.
- ENGINE_engine_process(&$variables, $hook): Allows the theme engine to
  process variables for all theme hooks with template implementations.
- ENGINE_engine_process_HOOK(&$variables): Allows the theme engine to process
  the variables specific to the theme hook.
- THEME_process(&$variables, $hook):  Allows the theme to process the
  variables for all theme hooks with template implementations.
- THEME_process_HOOK(&$variables):  Allows the theme to process the
  variables specific to the theme hook.

@subsection sub_preprocess_theme_funcs Preprocessing for Theme Functions
If the implementation is a function, only the theme-hook-specific preprocess
and process functions (the ones ending in _HOOK) are called from the
list above. This is because theme hooks with function implementations
need to be fast, and calling the non-theme-hook-specific preprocess and
process functions for them would incur a noticeable performance penalty.

@subsection sub_alternate_suggestions Suggesting Alternate Hooks
There are two special variables that these preprocess and process functions
can set: 'theme_hook_suggestion' and 'theme_hook_suggestions'. These will be
merged together to form a list of 'suggested' alternate theme hooks to use,
in reverse order of priority. theme_hook_suggestion will always be a higher
priority than items in theme_hook_suggestions. theme() will use the
highest priority implementation that exists. If none exists, theme() will
use the implementation for the theme hook it was called with. These
suggestions are similar to and are used for similar reasons as calling
theme() with an array as the $hook parameter (see below). The difference
is whether the suggestions are determined by the code that calls theme() or
by a preprocess or process function.

@param $hook
  The name of the theme hook to call. If the name contains a
  double-underscore ('__') and there isn't an implementation for the full
  name, the part before the '__' is checked. This allows a fallback to a
  more generic implementation. For example, if theme('links__node', ...) is
  called, but there is no implementation of that theme hook, then the
  'links' implementation is used. This process is iterative, so if
  theme('links__contextual__node', ...) is called, theme() checks for the
  following implementations, and uses the first one that exists:
  - links__contextual__node
  - links__contextual
  - links
  This allows themes to create specific theme implementations for named
  objects and contexts of otherwise generic theme hooks. The $hook parameter
  may also be an array, in which case the first theme hook that has an
  implementation is used. This allows for the code that calls theme() to
  explicitly specify the fallback order in a situation where using the '__'
  convention is not desired or is insufficient.
@param $variables
  An associative array of variables to merge with defaults from the theme
  registry, pass to preprocess and process functions for modification, and
  finally, pass to the function or template implementing the theme hook.
  Alternatively, this can be a renderable array, in which case, its
  properties are mapped to variables expected by the theme hook
  implementations.

@return
  An HTML string representing the themed output.

@see drupal_render()
@see themeable
@see hook_theme()
@see template_preprocess()
@see template_process()
```

## Code

```php
function theme($hook, $variables = array()) {
  // If called before all modules are loaded, we do not necessarily have a full
  // theme registry to work with, and therefore cannot process the theme
  // request properly. See also _theme_load_registry().
  if (!module_load_all(NULL) && !defined('MAINTENANCE_MODE')) {
    throw new Exception(t('theme() may not be called until all modules are loaded.'));
  }

  $hooks = theme_get_registry(FALSE);

  // If an array of hook candidates were passed, use the first one that has an
  // implementation.
  if (is_array($hook)) {
    foreach ($hook as $candidate) {
      if (isset($hooks[$candidate])) {
        break;
      }
    }
    $hook = $candidate;
  }
  $theme_hook_original = $hook;

  // If there's no implementation, check for more generic fallbacks. If there's
  // still no implementation, log an error and return an empty string.
  if (!isset($hooks[$hook])) {
    // Iteratively strip everything after the last '__' delimiter, until an
    // implementation is found.
    while ($pos = strrpos($hook, '__')) {
      $hook = substr($hook, 0, $pos);
      if (isset($hooks[$hook])) {
        break;
      }
    }
    if (!isset($hooks[$hook])) {
      // Only log a message when not trying theme suggestions ($hook being an
      // array).
      if (!isset($candidate)) {
        watchdog('theme', 'Theme hook %hook not found.', array('%hook' => $hook), WATCHDOG_WARNING);
      }
      return '';
    }
  }

  $info = $hooks[$hook];
  global $theme_path;
  $temp = $theme_path;
  // point path_to_theme() to the currently used theme path:
  $theme_path = $info['theme path'];

  // Include a file if the theme function or variable processor is held
  // elsewhere.
  if (!empty($info['includes'])) {
    foreach ($info['includes'] as $include_file) {
      include_once DRUPAL_ROOT . '/' . $include_file;
    }
  }

  // If a renderable array is passed as $variables, then set $variables to
  // the arguments expected by the theme function.
  if (isset($variables['#theme']) || isset($variables['#theme_wrappers'])) {
    $element = $variables;
    $variables = array();
    if (isset($info['variables'])) {
      foreach (array_keys($info['variables']) as $name) {
        if (isset($element["#$name"])) {
          $variables[$name] = $element["#$name"];
        }
      }
    }
    else {
      $variables[$info['render element']] = $element;
    }
  }

  // Merge in argument defaults.
  if (!empty($info['variables'])) {
    $variables += $info['variables'];
  }
  elseif (!empty($info['render element'])) {
    $variables += array($info['render element'] => array());
  }

  $variables['theme_hook_original'] = $theme_hook_original;

  // Invoke the variable processors, if any. The processors may specify
  // alternate suggestions for which hook's template/function to use. If the
  // hook is a suggestion of a base hook, invoke the variable processors of
  // the base hook, but retain the suggestion as a high priority suggestion to
  // be used unless overridden by a variable processor function.
  if (isset($info['base hook'])) {
    $base_hook = $info['base hook'];
    $base_hook_info = $hooks[$base_hook];
    // Include files required by the base hook, since its variable processors
    // might reside there.
    if (!empty($base_hook_info['includes'])) {
      foreach ($base_hook_info['includes'] as $include_file) {
        include_once DRUPAL_ROOT . '/' . $include_file;
      }
    }
    if (isset($base_hook_info['preprocess functions']) || isset($base_hook_info['process functions'])) {
      $variables['theme_hook_suggestion'] = $hook;
      $hook = $base_hook;
      $info = $base_hook_info;
    }
  }
  if (isset($info['preprocess functions']) || isset($info['process functions'])) {
    $variables['theme_hook_suggestions'] = array();
    foreach (array('preprocess functions', 'process functions') as $phase) {
      if (!empty($info[$phase])) {
        foreach ($info[$phase] as $processor_function) {
          if (function_exists($processor_function)) {
            // We don't want a poorly behaved process function changing $hook.
            $hook_clone = $hook;
            $processor_function($variables, $hook_clone);
          }
        }
      }
    }
    // If the preprocess/process functions specified hook suggestions, and the
    // suggestion exists in the theme registry, use it instead of the hook that
    // theme() was called with. This allows the preprocess/process step to
    // route to a more specific theme hook. For example, a function may call
    // theme('node', ...), but a preprocess function can add 'node__article' as
    // a suggestion, enabling a theme to have an alternate template file for
    // article nodes. Suggestions are checked in the following order:
    // - The 'theme_hook_suggestion' variable is checked first. It overrides
    //   all others.
    // - The 'theme_hook_suggestions' variable is checked in FILO order, so the
    //   last suggestion added to the array takes precedence over suggestions
    //   added earlier.
    $suggestions = array();
    if (!empty($variables['theme_hook_suggestions'])) {
      $suggestions = $variables['theme_hook_suggestions'];
    }
    if (!empty($variables['theme_hook_suggestion'])) {
      $suggestions[] = $variables['theme_hook_suggestion'];
    }
    foreach (array_reverse($suggestions) as $suggestion) {
      if (isset($hooks[$suggestion])) {
        $info = $hooks[$suggestion];
        break;
      }
    }
  }

  // Generate the output using either a function or a template.
  $output = '';
  if (isset($info['function'])) {
    if (function_exists($info['function'])) {
      $output = $info['function']($variables);
    }
  }
  else {
    // Default render function and extension.
    $render_function = 'theme_render_template';
    $extension = '.tpl.php';

    // The theme engine may use a different extension and a different renderer.
    global $theme_engine;
    if (isset($theme_engine)) {
      if ($info['type'] != 'module') {
        if (function_exists($theme_engine . '_render_template')) {
          $render_function = $theme_engine . '_render_template';
        }
        $extension_function = $theme_engine . '_extension';
        if (function_exists($extension_function)) {
          $extension = $extension_function();
        }
      }
    }

    // In some cases, a template implementation may not have had
    // template_preprocess() run (for example, if the default implementation is
    // a function, but a template overrides that default implementation). In
    // these cases, a template should still be able to expect to have access to
    // the variables provided by template_preprocess(), so we add them here if
    // they don't already exist. We don't want to run template_preprocess()
    // twice (it would be inefficient and mess up zebra striping), so we use the
    // 'directory' variable to determine if it has already run, which while not
    // completely intuitive, is reasonably safe, and allows us to save on the
    // overhead of adding some new variable to track that.
    if (!isset($variables['directory'])) {
      $default_template_variables = array();
      template_preprocess($default_template_variables, $hook);
      $variables += $default_template_variables;
    }

    // Render the output using the template file.
    $template_file = $info['template'] . $extension;
    if (isset($info['path'])) {
      $template_file = $info['path'] . '/' . $template_file;
    }
    if (variable_get('theme_debug', FALSE)) {
      $output = _theme_render_template_debug($render_function, $template_file, $variables, $extension);
    }
    else {
      $output = $render_function($template_file, $variables);
    }
  }

  // restore path_to_theme()
  $theme_path = $temp;
  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
