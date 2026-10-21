# hook_library_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 842–854 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L842-L854)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_library_alter(&$libraries, $module)
```

## Documentation

```text
Alters the JavaScript/CSS library registry.

Allows certain, contributed modules to update libraries to newer versions
while ensuring backwards compatibility. In general, such manipulations should
only be done by designated modules, since most modules that integrate with a
certain library also depend on the API of a certain library version.

@param $libraries
  The JavaScript/CSS libraries provided by $module. Keyed by internal library
  name and passed by reference.
@param $module
  The name of the module that registered the libraries.

@see hook_library()
```

## Code

```php
function hook_library_alter(&$libraries, $module) {
  // Update Farbtastic to version 2.0.
  if ($module == 'system' && isset($libraries['farbtastic'])) {
    // Verify existing version is older than the one we are updating to.
    if (version_compare($libraries['farbtastic']['version'], '2.0', '<')) {
      // Update the existing Farbtastic to version 2.0.
      $libraries['farbtastic']['version'] = '2.0';
      $libraries['farbtastic']['js'] = array(
        drupal_get_path('module', 'farbtastic_update') . '/farbtastic-2.0.js' => array(),
      );
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_library_alter()".

- [common_test_library_alter()](../../simpletest/tests/common_test.module/common_test_library_alter.md) — `modules/simpletest/tests/common_test.module`
- [locale_library_alter()](../../locale/locale.module/locale_library_alter.md) — `modules/locale/locale.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
