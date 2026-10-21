# system_get_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2369–2384 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2369-L2384)
- **Module/theme:** system

## Signature

```php
function system_get_info($type, $name = NULL)
```

## Documentation

```text
Returns an array of information about enabled modules or themes.

This function returns the information from the {system} table corresponding
to the cached contents of the .info file for each active module or theme.

@param $type
  Either 'module' or 'theme'.
@param $name
  (optional) The name of a module or theme whose information shall be
  returned. If omitted, all records for the provided $type will be returned.
  If $name does not exist in the provided $type or is not enabled, an empty
  array will be returned.

@return
  An associative array of module or theme information keyed by name, or only
  information for $name, if given. If no records are available, an empty
  array is returned.

@see system_rebuild_module_data()
@see system_rebuild_theme_data()
```

## Code

```php
function system_get_info($type, $name = NULL) {
  $info = array();
  if ($type == 'module') {
    $type = 'module_enabled';
  }
  $list = system_list($type);
  foreach ($list as $shortname => $item) {
    if (!empty($item->status)) {
      $info[$shortname] = $item->info;
    }
  }
  if (isset($name)) {
    return isset($info[$name]) ? $info[$name] : array();
  }
  return $info;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
