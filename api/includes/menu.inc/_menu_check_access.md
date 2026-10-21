# _menu_check_access()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 631–651 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L631-L651)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_check_access(&$item, $map)
```

## Documentation

```text
Checks access to a menu item using the access callback.

@param $item
  A menu router or menu link item
@param $map
  An array of path arguments; for example, array('node', '5').

@return
  $item['access'] becomes TRUE if the item is accessible, FALSE otherwise.
```

## Code

```php
function _menu_check_access(&$item, $map) {
  $item['access'] = FALSE;
  // Determine access callback, which will decide whether or not the current
  // user has access to this path.
  $callback = empty($item['access_callback']) ? 0 : trim($item['access_callback']);
  // Check for a TRUE or FALSE value.
  if (is_numeric($callback)) {
    $item['access'] = (bool) $callback;
  }
  else {
    $arguments = menu_unserialize($item['access_arguments'], $map);
    // As call_user_func_array is quite slow and user_access is a very common
    // callback, it is worth making a special case for it.
    if ($callback == 'user_access') {
      $item['access'] = (count($arguments) == 1) ? user_access($arguments[0]) : user_access($arguments[0], $arguments[1]);
    }
    elseif (function_exists($callback)) {
      $item['access'] = call_user_func_array($callback, $arguments);
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
