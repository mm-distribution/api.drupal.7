# hook_library()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 786–824 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L786-L824)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_library()
```

## Documentation

```text
Registers JavaScript/CSS libraries associated with a module.

Modules implementing this return an array of arrays. The key to each
sub-array is the machine readable name of the library. Each library may
contain the following items:

- 'title': The human readable name of the library.
- 'website': The URL of the library's web site.
- 'version': A string specifying the version of the library; intentionally
  not a float because a version like "1.2.3" is not a valid float. Use PHP's
  version_compare() to compare different versions.
- 'js': An array of JavaScript elements; each element's key is used as $data
  argument, each element's value is used as $options array for
  drupal_add_js(). To add library-specific (not module-specific) JavaScript
  settings, the key may be skipped, the value must specify
  'type' => 'setting', and the actual settings must be contained in a 'data'
  element of the value.
- 'css': Like 'js', an array of CSS elements passed to drupal_add_css().
- 'dependencies': An array of libraries that are required for a library. Each
  element is an array listing the module and name of another library. Note
  that all dependencies for each dependent library will also be added when
  this library is added.

Registered information for a library should contain re-usable data only.
Module- or implementation-specific data and integration logic should be added
separately.

@return
  An array defining libraries associated with a module.

@see system_library()
@see drupal_add_library()
@see drupal_get_library()
```

## Code

```php
function hook_library() {
  // Library One.
  $libraries['library-1'] = array(
    'title' => 'Library One',
    'website' => 'http://example.com/library-1',
    'version' => '1.2',
    'js' => array(
      drupal_get_path('module', 'my_module') . '/library-1.js' => array(),
    ),
    'css' => array(
      drupal_get_path('module', 'my_module') . '/library-2.css' => array(
        'type' => 'file',
        'media' => 'screen',
      ),
    ),
  );
  // Library Two.
  $libraries['library-2'] = array(
    'title' => 'Library Two',
    'website' => 'http://example.com/library-2',
    'version' => '3.1-beta1',
    'js' => array(
      // JavaScript settings may use the 'data' key.
      array(
        'type' => 'setting',
        'data' => array('library2' => TRUE),
      ),
    ),
    'dependencies' => array(
      // Require jQuery UI core by System module.
      array('system', 'ui'),
      // Require our other library.
      array('my_module', 'library-1'),
      // Require another library.
      array('other_module', 'library-3'),
    ),
  );
  return $libraries;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_library()".

- [common_test_library()](../../simpletest/tests/common_test.module/common_test_library.md) — `modules/simpletest/tests/common_test.module`
- [contextual_library()](../../contextual/contextual.module/contextual_library.md) — `modules/contextual/contextual.module`
- [overlay_library()](../../overlay/overlay.module/overlay_library.md) — `modules/overlay/overlay.module`
- [system_library()](../system.module/system_library.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
