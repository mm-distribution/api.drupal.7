# _field_ui_view_mode_menu_access()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 267–300 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L267-L300)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_view_mode_menu_access($entity_type, $bundle, $view_mode, $access_callback)
```

## Documentation

```text
Menu access callback for the 'view mode display settings' pages.
```

## Code

```php
function _field_ui_view_mode_menu_access($entity_type, $bundle, $view_mode, $access_callback) {
  // It's good practice to call func_get_args() at the beginning of a function
  // to avoid problems with function parameters being modified later. The
  // behavior of func_get_args() changed in PHP7.
  // @see https://www.php.net/manual/en/migration70.incompatible.php#migration70.incompatible.other.func-parameter-modified
  $all_args = func_get_args();

  // First, determine visibility according to the 'use custom display'
  // setting for the view mode.
  $bundle = field_extract_bundle($entity_type, $bundle);
  $view_mode_settings = field_view_mode_settings($entity_type, $bundle);
  $visibility = ($view_mode == 'default') || !empty($view_mode_settings[$view_mode]['custom_settings']);

  // Then, determine access according to the $access parameter. This duplicates
  // part of _menu_check_access().
  if ($visibility) {
    // Grab the variable 'access arguments' part.
    $args = array_slice($all_args, 4);
    $callback = empty($access_callback) ? 0 : trim($access_callback);
    if (is_numeric($callback)) {
      return (bool) $callback;
    }
    else {
      // As call_user_func_array() is quite slow and user_access is a very
      // common callback, it is worth making a special case for it.
      if ($access_callback == 'user_access') {
        return (count($args) == 1) ? user_access($args[0]) : user_access($args[0], $args[1]);
      }
      elseif (function_exists($access_callback)) {
        return call_user_func_array($access_callback, $args);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
