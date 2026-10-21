# module_load_include()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 327–351 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L327-L351)

## Signature

```php
function module_load_include($type, $module, $name = NULL)
```

## Documentation

```text
Loads a module include file.

Examples:
@code
  // Load node.admin.inc from the node module.
  module_load_include('inc', 'node', 'node.admin');
  // Load content_types.inc from the node module.
  module_load_include('inc', 'node', 'content_types');
@endcode

Do not use this function to load an install file, use module_load_install()
instead. Do not use this function in a global context since it requires
Drupal to be fully bootstrapped, use require_once DRUPAL_ROOT . '/path/file'
instead.

@param $type
  The include file's type (file extension).
@param $module
  The module to which the include file belongs.
@param $name
  (optional) The base file name (without the $type extension). If omitted,
  $module is used; i.e., resulting in "$module.$type" by default.

@return
  The name of the included file, if successful; FALSE otherwise.
```

## Code

```php
function module_load_include($type, $module, $name = NULL) {
  static $files = array();

  if (!isset($name)) {
    $name = $module;
  }

  $key = $type . ':' . $module . ':' . $name;
  if (isset($files[$key])) {
    return $files[$key];
  }

  if (function_exists('drupal_get_path')) {
    $file = DRUPAL_ROOT . '/' . drupal_get_path('module', $module) . "/$name.$type";
    if (is_file($file)) {
      require_once $file;
      $files[$key] = $file;
      return $file;
    }
    else {
      $files[$key] = FALSE;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
