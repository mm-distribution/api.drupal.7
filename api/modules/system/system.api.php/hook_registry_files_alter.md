# hook_registry_files_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3712–3725 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3712-L3725)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_registry_files_alter(&$files, $modules)
```

## Documentation

```text
Perform necessary alterations to the list of files parsed by the registry.

Modules can manually modify the list of files before the registry parses
them. The $modules array provides the .info file information, which includes
the list of files registered to each module. Any files in the list can then
be added to the list of files that the registry will parse, or modify
attributes of a file.

A necessary alteration made by the core SimpleTest module is to force .test
files provided by disabled modules into the list of files parsed by the
registry.

@param $files
  List of files to be parsed by the registry. The list will contain
  files found in each enabled module's info file and the core includes
  directory. The array is keyed by the file path and contains an array of
  the related module's name and weight as used internally by
  _registry_update() and related functions.

  For example:
  @code
    $files["modules/system/system.module"] = array(
      'module' => 'system',
      'weight' => 0,
    );
  @endcode
@param $modules
  An array containing all module information stored in the {system} table.
  Each element of the array also contains the module's .info file
  information in the property 'info'. An additional 'dir' property has been
  added to the module information which provides the path to the directory
  in which the module resides. The example shows how to take advantage of
  both properties.

@see _registry_update()
@see simpletest_test_get_all()
```

## Code

```php
function hook_registry_files_alter(&$files, $modules) {
  foreach ($modules as $module) {
    // Only add test files for disabled modules, as enabled modules should
    // already include any test files they provide.
    if (!$module->status) {
      $dir = $module->dir;
      foreach ($module->info['files'] as $file) {
        if (substr($file, -5) == '.test') {
          $files["$dir/$file"] = array('module' => $module->name, 'weight' => $module->weight);
        }
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_registry_files_alter()".

- [drupal_autoload_test_registry_files_alter()](../../simpletest/tests/drupal_autoload_test/drupal_autoload_test.module/drupal_autoload_test_registry_files_alter.md) — `modules/simpletest/tests/drupal_autoload_test/drupal_autoload_test.module`
- [simpletest_registry_files_alter()](../../simpletest/simpletest.module/simpletest_registry_files_alter.md) — `modules/simpletest/simpletest.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
