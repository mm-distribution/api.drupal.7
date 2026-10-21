# simpletest_script_get_test_list()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 493–614 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L493-L614)

## Signature

```php
function simpletest_script_get_test_list()
```

## Documentation

```text
Get list of tests based on arguments. If --all specified then
returns all available tests, otherwise reads list of tests.

Will print error and exit if no valid tests were found.

@return List of tests.
```

## Code

```php
function simpletest_script_get_test_list() {
  global $args, $all_tests, $groups;

  $test_list = array();
  if ($args['all']) {
    $test_list = $all_tests;
  }
  else {
    if ($args['class']) {
      // Check for valid class names.
      $test_list = array();
      foreach ($args['test_names'] as $test_class) {
        list($class_name, $method) = explode('::', $test_class, 2);
        if (class_exists($class_name)) {
          if (empty($method) || method_exists($class_name, $method)) {
            $test_list[] = $test_class;
          } else {
            $all_methods = get_class_methods($class_name);
            simpletest_script_print_error('Test method not found: ' . $test_class);
            simpletest_script_print_alternatives($method, $all_methods, 6);
            exit(1);
          }
        }
        else {
          $groups = simpletest_test_get_all();
          $all_classes = array();
          foreach ($groups as $group) {
            $all_classes = array_merge($all_classes, array_keys($group));
          }
          simpletest_script_print_error('Test class not found: ' . $class_name);
          simpletest_script_print_alternatives($class_name, $all_classes, 6);
          exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
        }
      }
    }
    elseif ($args['file']) {
      $files = array();
      foreach ($args['test_names'] as $file) {
        $files[drupal_realpath($file)] = 1;
      }

      // Check for valid class names.
      foreach ($all_tests as $class_name) {
        $refclass = new ReflectionClass($class_name);
        $file = $refclass->getFileName();
        if (isset($files[$file])) {
          $test_list[] = $class_name;
        }
      }
    }
    elseif ($args['directory']) {
      // Extract test case class names from specified directory.
      // Find all tests in the PSR-X structure; Drupal\$extension\Tests\*.php
      // Since we do not want to hard-code too many structural file/directory
      // assumptions about PSR-0/4 files and directories, we check for the
      // minimal conditions only; i.e., a '*.php' file that has '/Tests/' in
      // its path.
      // Ignore anything from third party vendors, and ignore template files used in tests.
      // And any api.php files.
      $ignore = array('nomask' => '/vendor|\.tpl\.php|\.api\.php/');
      $files = array();
      if ($args['directory'][0] === '/') {
        $directory = $args['directory'];
      }
      else {
        $directory = DRUPAL_ROOT . "/" . $args['directory'];
      }
      $file_list = file_scan_directory($directory, '/\.php|\.test$/', $ignore);
      foreach ($file_list as $file) {
        // '/Tests/' can be contained anywhere in the file's path (there can be
        // sub-directories below /Tests), but must be contained literally.
        // Case-insensitive to match all Simpletest and PHPUnit tests:
        //   ./lib/Drupal/foo/Tests/Bar/Baz.php
        //   ./foo/src/Tests/Bar/Baz.php
        //   ./foo/tests/Drupal/foo/Tests/FooTest.php
        //   ./foo/tests/src/FooTest.php
        // $file->filename doesn't give us a directory, so we use $file->uri
        // Strip the drupal root directory and trailing slash off the URI
        $filename = substr($file->uri, strlen(DRUPAL_ROOT)+1);
        if (stripos($filename, '/Tests/')) {
          $files[drupal_realpath($filename)] = 1;
        } else if (stripos($filename, '.test')){
          $files[drupal_realpath($filename)] = 1;
        }
      }

      // Check for valid class names.
      foreach ($all_tests as $class_name) {
        $refclass = new ReflectionClass($class_name);
        $classfile = $refclass->getFileName();
        if (isset($files[$classfile])) {
          $test_list[] = $class_name;
        }
      }
    }
    else {
      // Check for valid group names and get all valid classes in group.
      foreach ($args['test_names'] as $group_name) {
        if (isset($groups[$group_name])) {
          $test_list = array_merge($test_list, array_keys($groups[$group_name]));
        }
        else {
          simpletest_script_print_error('Test group not found: ' . $group_name);
          simpletest_script_print_alternatives($group_name, array_keys($groups));
          exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
        }
      }
    }
  }

  if (empty($test_list)) {
    simpletest_script_print_error('No valid tests were specified.');
    exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
  }

  if ((int) $args['ci-parallel-node-total'] > 1) {
    $tests_per_job = ceil(count($test_list) / $args['ci-parallel-node-total']);
    $test_list = array_slice($test_list, ($args['ci-parallel-node-index'] - 1) * $tests_per_job, $tests_per_job);
  }

  return $test_list;
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
