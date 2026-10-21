# menu_get_custom_theme()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1764–1788 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1764-L1788)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_custom_theme($initialize = FALSE)
```

## Documentation

```text
Gets the custom theme for the current page, if there is one.

@param $initialize
  This parameter should only be used internally; it is set to TRUE in order
  to force the custom theme to be initialized for the current page request.

@return
  The machine-readable name of the custom theme, if there is one.

@see menu_set_custom_theme()
```

## Code

```php
function menu_get_custom_theme($initialize = FALSE) {
  $custom_theme = &drupal_static(__FUNCTION__);
  // Skip this if the site is offline or being installed or updated, since the
  // menu system may not be correctly initialized then.
  if ($initialize && !_menu_site_is_offline(TRUE) && (!defined('MAINTENANCE_MODE') || (MAINTENANCE_MODE != 'update' && MAINTENANCE_MODE != 'install'))) {
    // First allow modules to dynamically set a custom theme for the current
    // page. Since we can only have one, the last module to return a valid
    // theme takes precedence.
    $custom_themes = array_filter(module_invoke_all('custom_theme'), 'drupal_theme_access');
    if (!empty($custom_themes)) {
      $custom_theme = array_pop($custom_themes);
    }
    // If there is a theme callback function for the current page, execute it.
    // If this returns a valid theme, it will override any theme that was set
    // by a hook_custom_theme() implementation above.
    $router_item = menu_get_item();
    if (!empty($router_item['access']) && !empty($router_item['theme_callback']) && function_exists($router_item['theme_callback'])) {
      $theme_name = call_user_func_array($router_item['theme_callback'], $router_item['theme_arguments']);
      if (drupal_theme_access($theme_name)) {
        $custom_theme = $theme_name;
      }
    }
  }
  return $custom_theme;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
