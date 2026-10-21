# simpletest_test_get_all()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 315–402 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L315-L402)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_test_get_all()
```

## Documentation

```text
Get a list of all of the tests provided by the system.

The list of test classes is loaded from the registry where it looks for
files ending in ".test". Once loaded the test list is cached and stored in
a static variable. In order to list tests provided by disabled modules
hook_registry_files_alter() is used to forcefully add them to the registry.

PSR-0 classes are found by searching the designated directory for each module
for files matching the PSR-0 standard.

@return
  An array of tests keyed with the groups specified in each of the tests
  getInfo() method and then keyed by the test class. An example of the array
  structure is provided below.

  @code
    $groups['Blog'] => array(
      'BlogTestCase' => array(
        'name' => 'Blog functionality',
        'description' => 'Create, view, edit, delete, ...',
        'group' => 'Blog',
      ),
    );
  @endcode
@see simpletest_registry_files_alter()
```

## Code

```php
function simpletest_test_get_all() {
  $groups = &drupal_static(__FUNCTION__);

  if (!$groups) {
    // Register a simple class loader for PSR-0 test classes.
    simpletest_classloader_register();

    // Load test information from cache if available, otherwise retrieve the
    // information from each tests getInfo() method.
    if ($cache = cache_get('simpletest', 'cache')) {
      $groups = $cache->data;
    }
    else {
      // Select all classes in files ending with .test.
      $classes = db_query("SELECT name FROM {registry} WHERE type = :type AND filename LIKE :name", array(':type' => 'class', ':name' => '%.test'))->fetchCol();

      // Also discover PSR-0 test classes, if the PHP version allows it.
      if (version_compare(PHP_VERSION, '5.3') > 0) {

        // Select all PSR-0 and PSR-4 classes in the Tests namespace of all
        // modules.
        $system_list = db_query("SELECT name, filename FROM {system}")->fetchAllKeyed();

        foreach ($system_list as $name => $filename) {
          $module_dir = DRUPAL_ROOT . '/' . dirname($filename);
          // Search both the 'lib/Drupal/mymodule' directory (for PSR-0 classes)
          // and the 'src' directory (for PSR-4 classes).
          foreach(array('lib/Drupal/' . $name, 'src') as $subdir) {
            // Build directory in which the test files would reside.
            $tests_dir = $module_dir . '/' . $subdir . '/Tests';
            // Scan it for test files if it exists.
            if (is_dir($tests_dir)) {
              $files = file_scan_directory($tests_dir, '/.*\.php/');
              if (!empty($files)) {
                foreach ($files as $file) {
                  // Convert the file name into the namespaced class name.
                  $replacements = array(
                    '/' => '\\',
                    $module_dir . '/' => '',
                    'lib/' => '',
                    'src/' => 'Drupal\\' . $name . '\\',
                    '.php' => '',
                  );
                  $classes[] = strtr($file->uri, $replacements);
                }
              }
            }
          }
        }
      }

      // Check that each class has a getInfo() method and store the information
      // in an array keyed with the group specified in the test information.
      $groups = array();
      foreach ($classes as $class) {
        // Test classes need to implement getInfo() to be valid.
        if (class_exists($class) && method_exists($class, 'getInfo')) {
          $info = call_user_func(array($class, 'getInfo'));

          // If this test class requires a non-existing module, skip it.
          if (!empty($info['dependencies'])) {
            foreach ($info['dependencies'] as $module) {
              // Pass FALSE as fourth argument so no error gets created for
              // the missing file.
              $found_module = drupal_get_filename('module', $module, NULL, FALSE);
              if (!$found_module) {
                continue 2;
              }
            }
          }

          $groups[$info['group']][$class] = $info;
        }
      }

      // Sort the groups and tests within the groups by name.
      uksort($groups, 'strnatcasecmp');
      foreach ($groups as $group => &$tests) {
        uksort($tests, 'strnatcasecmp');
      }

      // Allow modules extending core tests to disable originals.
      drupal_alter('simpletest', $groups);
      cache_set('simpletest', $groups);
    }
  }
  return $groups;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
