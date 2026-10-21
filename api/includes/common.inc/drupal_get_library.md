# drupal_get_library()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5026–5056 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5026-L5056)

## Signature

```php
function drupal_get_library($module, $name = NULL)
```

## Documentation

```text
Retrieves information for a JavaScript/CSS library.

Library information is statically cached. Libraries are keyed by module for
several reasons:
- Libraries are not unique. Multiple modules might ship with the same library
  in a different version or variant. This registry cannot (and does not
  attempt to) prevent library conflicts.
- Modules implementing and thereby depending on a library that is registered
  by another module can only rely on that module's library.
- Two (or more) modules can still register the same library and use it
  without conflicts in case the libraries are loaded on certain pages only.

@param $module
  The name of a module that registered a library.
@param $name
  (optional) The name of a registered library to retrieve. By default, all
  libraries registered by $module are returned.

@return
  The definition of the requested library, if $name was passed and it exists,
  or FALSE if it does not exist. If no $name was passed, an associative array
  of libraries registered by $module is returned (which may be empty).

@see drupal_add_library()
@see hook_library()
@see hook_library_alter()

@todo The purpose of drupal_get_*() is completely different to other page
  requisite API functions; find and use a different name.
```

## Code

```php
function drupal_get_library($module, $name = NULL) {
  $libraries = &drupal_static(__FUNCTION__, array());

  if (!isset($libraries[$module])) {
    // Retrieve all libraries associated with the module.
    $module_libraries = module_invoke($module, 'library');
    if (empty($module_libraries)) {
      $module_libraries = array();
    }
    // Allow modules to alter the module's registered libraries.
    drupal_alter('library', $module_libraries, $module);

    foreach ($module_libraries as $key => $data) {
      if (is_array($data)) {
        // Add default elements to allow for easier processing.
        $module_libraries[$key] += array('dependencies' => array(), 'js' => array(), 'css' => array());
        foreach ($module_libraries[$key]['js'] as $file => $options) {
          $module_libraries[$key]['js'][$file]['version'] = $module_libraries[$key]['version'];
        }
      }
    }
    $libraries[$module] = $module_libraries;
  }
  if (isset($name)) {
    if (!isset($libraries[$module][$name])) {
      $libraries[$module][$name] = FALSE;
    }
    return $libraries[$module][$name];
  }
  return $libraries[$module];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
