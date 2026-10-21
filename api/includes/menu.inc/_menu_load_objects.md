# _menu_load_objects()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 564–618 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L564-L618)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_load_objects(&$item, &$map)
```

## Documentation

```text
Loads objects into the map as defined in the $item['load_functions'].

@param $item
  A menu router or menu link item
@param $map
  An array of path arguments; for example, array('node', '5').

@return
  Returns TRUE for success, FALSE if an object cannot be loaded.
  Names of object loading functions are placed in $item['load_functions'].
  Loaded objects are placed in $map[]; keys are the same as keys in the
  $item['load_functions'] array.
  $item['access'] is set to FALSE if an object cannot be loaded.
```

## Code

```php
function _menu_load_objects(&$item, &$map) {
  if ($load_functions = $item['load_functions']) {
    // If someone calls this function twice, then unserialize will fail.
    if (!is_array($load_functions)) {
      $load_functions = unserialize($load_functions);
    }
    $path_map = $map;
    foreach ($load_functions as $index => $function) {
      if ($function) {
        $value = isset($path_map[$index]) ? $path_map[$index] : '';
        if (is_array($function)) {
          // Set up arguments for the load function. These were pulled from
          // 'load arguments' in the hook_menu() entry, but they need
          // some processing. In this case the $function is the key to the
          // load_function array, and the value is the list of arguments.
          $args = current($function);
          $function = key($function);
          $load_functions[$index] = $function;

          // Some arguments are placeholders for dynamic items to process.
          foreach ($args as $i => $arg) {
            if ($arg === '%index') {
              // Pass on argument index to the load function, so multiple
              // occurrences of the same placeholder can be identified.
              $args[$i] = $index;
            }
            if ($arg === '%map') {
              // Pass on menu map by reference. The accepting function must
              // also declare this as a reference if it wants to modify
              // the map.
              $args[$i] = &$map;
            }
            if (is_int($arg)) {
              $args[$i] = isset($path_map[$arg]) ? $path_map[$arg] : '';
            }
          }
          array_unshift($args, $value);
          $return = call_user_func_array($function, $args);
        }
        else {
          $return = $function($value);
        }
        // If callback returned an error or there is no callback, trigger 404.
        if ($return === FALSE) {
          $item['access'] = FALSE;
          $map = FALSE;
          return FALSE;
        }
        $map[$index] = $return;
      }
    }
    $item['load_functions'] = $load_functions;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
