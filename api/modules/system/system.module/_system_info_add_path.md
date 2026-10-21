# _system_info_add_path()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2693–2707 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2693-L2707)
- **Module/theme:** system

## Signature

```php
function _system_info_add_path($info, $path)
```

## Documentation

```text
Prefixes all values in an .info file array with a given path.

This helper function is mainly used to prefix all array values of an .info
file property with a single given path (to the module or theme); e.g., to
prefix all values of the 'stylesheets' or 'scripts' properties with the file
path to the defining module/theme.

@param $info
  A nested array of data of an .info file to be processed.
@param $path
  A file path to prepend to each value in $info.

@return
  The $info array with prefixed values.

@see _system_rebuild_module_data()
@see _system_rebuild_theme_data()
```

## Code

```php
function _system_info_add_path($info, $path) {
  foreach ($info as $key => $value) {
    // Recurse into nested values until we reach the deepest level.
    if (is_array($value)) {
      $info[$key] = _system_info_add_path($info[$key], $path);
    }
    // Unset the original value's key and set the new value with prefix, using
    // the original value as key, so original values can still be looked up.
    else {
      unset($info[$key]);
      $info[$value] = $path . '/' . $value;
    }
  }
  return $info;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
