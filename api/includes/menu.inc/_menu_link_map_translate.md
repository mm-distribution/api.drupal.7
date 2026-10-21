# _menu_link_map_translate()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 821–833 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L821-L833)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_map_translate(&$map, $to_arg_functions)
```

## Documentation

```text
Translates the path elements in the map using any to_arg helper function.

@param $map
  An array of path arguments; for example, array('node', '5').
@param $to_arg_functions
  An array of helper functions; for example, array(2 => 'menu_tail_to_arg').

@see hook_menu()
```

## Code

```php
function _menu_link_map_translate(&$map, $to_arg_functions) {
  $to_arg_functions = unserialize($to_arg_functions);
  foreach ($to_arg_functions as $index => $function) {
    // Translate place-holders into real values.
    $arg = $function(!empty($map[$index]) ? $map[$index] : '', $map, $index);
    if (!empty($map[$index]) || isset($arg)) {
      $map[$index] = $arg;
    }
    else {
      unset($map[$index]);
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
