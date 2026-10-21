# module_list()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 66–102 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L66-L102)

## Signature

```php
function module_list($refresh = FALSE, $bootstrap_refresh = FALSE, $sort = FALSE, $fixed_list = NULL)
```

## Documentation

```text
Returns a list of currently active modules.

Usually, this returns a list of all enabled modules. When called early on in
the bootstrap, it will return a list of vital modules only (those needed to
generate cached pages).

All parameters to this function are optional and should generally not be
changed from their defaults.

@param $refresh
  (optional) Whether to force the module list to be regenerated (such as
  after the administrator has changed the system settings). Defaults to
  FALSE.
@param $bootstrap_refresh
  (optional) When $refresh is TRUE, setting $bootstrap_refresh to TRUE forces
  the module list to be regenerated using the reduced set of modules loaded
  in "bootstrap mode" for cached pages. Otherwise, setting $refresh to TRUE
  generates the complete list of enabled modules.
@param $sort
  (optional) By default, modules are ordered by weight and module name. Set
  this option to TRUE to return a module list ordered only by module name.
@param $fixed_list
  (optional) If an array of module names is provided, this will override the
  module list with the given set of modules. This will persist until the next
  call with $refresh set to TRUE or with a new $fixed_list passed in. This
  parameter is primarily intended for internal use (e.g., in install.php and
  update.php).

@return
  An associative array whose keys and values are the names of the modules in
  the list.
```

## Code

```php
function module_list($refresh = FALSE, $bootstrap_refresh = FALSE, $sort = FALSE, $fixed_list = NULL) {
  static $list = array(), $sorted_list;

  if (empty($list) || $refresh || $fixed_list) {
    $list = array();
    $sorted_list = NULL;
    if ($fixed_list) {
      foreach ($fixed_list as $name => $module) {
        drupal_get_filename('module', $name, $module['filename']);
        $list[$name] = $name;
      }
    }
    else {
      if ($refresh) {
        // For the $refresh case, make sure that system_list() returns fresh
        // data.
        drupal_static_reset('system_list');
      }
      if ($bootstrap_refresh) {
        $list = system_list('bootstrap');
      }
      else {
        // Not using drupal_map_assoc() here as that requires common.inc.
        $list = array_keys(system_list('module_enabled'));
        $list = (!empty($list) ? array_combine($list, $list) : array());
      }
    }
  }
  if ($sort) {
    if (!isset($sorted_list)) {
      $sorted_list = $list;
      ksort($sorted_list);
    }
    return $sorted_list;
  }
  return $list;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
