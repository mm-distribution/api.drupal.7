# drupal_find_theme_functions()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1248–1293 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1248-L1293)

## Signature

```php
function drupal_find_theme_functions($cache, $prefixes)
```

## Documentation

```text
Allows themes and/or theme engines to discover overridden theme functions.

@param $cache
  The existing cache of theme hooks to test against.
@param $prefixes
  An array of prefixes to test, in reverse order of importance.

@return $implementations
  The functions found, suitable for returning from hook_theme;
```

## Code

```php
function drupal_find_theme_functions($cache, $prefixes) {
  $implementations = array();
  $functions = get_defined_functions();
  $theme_functions = preg_grep('/^(' . implode(')|(', $prefixes) . ')_/', $functions['user']);

  foreach ($cache as $hook => $info) {
    foreach ($prefixes as $prefix) {
      // Find theme functions that implement possible "suggestion" variants of
      // registered theme hooks and add those as new registered theme hooks.
      // The 'pattern' key defines a common prefix that all suggestions must
      // start with. The default is the name of the hook followed by '__'. An
      // 'base hook' key is added to each entry made for a found suggestion,
      // so that common functionality can be implemented for all suggestions of
      // the same base hook. To keep things simple, deep hierarchy of
      // suggestions is not supported: each suggestion's 'base hook' key
      // refers to a base hook, not to another suggestion, and all suggestions
      // are found using the base hook's pattern, not a pattern from an
      // intermediary suggestion.
      $pattern = isset($info['pattern']) ? $info['pattern'] : ($hook . '__');
      if (!isset($info['base hook']) && !empty($pattern)) {
        $matches = preg_grep('/^' . $prefix . '_' . $pattern . '/', $theme_functions);
        if ($matches) {
          foreach ($matches as $match) {
            $new_hook = substr($match, strlen($prefix) + 1);
            $arg_name = isset($info['variables']) ? 'variables' : 'render element';
            $implementations[$new_hook] = array(
              'function' => $match,
              $arg_name => $info[$arg_name],
              'base hook' => $hook,
            );
          }
        }
      }
      // Find theme functions that implement registered theme hooks and include
      // that in what is returned so that the registry knows that the theme has
      // this implementation.
      if (function_exists($prefix . '_' . $hook)) {
        $implementations[$hook] = array(
          'function' => $prefix . '_' . $hook,
        );
      }
    }
  }

  return $implementations;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
