# simpletest_script_run_one_test()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 418–457 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L418-L457)

## Signature

```php
function simpletest_script_run_one_test($test_id, $test_class)
```

## Documentation

```text
Bootstrap Drupal and run a single test.
```

## Code

```php
function simpletest_script_run_one_test($test_id, $test_class) {
  global $args;

  try {
    // Bootstrap Drupal.
    drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

    simpletest_classloader_register();

    if (strpos($test_class, '::') > 0) {
      list($class_name, $method) = explode('::', $test_class, 2);
      $methods = array($method);
    }
    else {
      $class_name = $test_class;
      // Use empty array to run all the test methods.
      $methods = array();
    }
    $test = new $class_name($test_id);
    $test->useSetupInstallationCache = !empty($args['cache']);
    $test->useSetupModulesCache = !empty($args['cache-modules']);
    $test->run($methods);
    $info = $test->getInfo();

    $had_fails = (isset($test->results['#fail']) && $test->results['#fail'] > 0);
    $had_exceptions = (isset($test->results['#exception']) && $test->results['#exception'] > 0);
    $status = ($had_fails || $had_exceptions ? 'fail' : 'pass');
    simpletest_script_print($info['name'] . ' ' . _simpletest_format_summary_line($test->results) . "\n", simpletest_script_color_code($status));

    // Finished, kill this runner.
    if ($had_fails || $had_exceptions) {
      exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
    }
    exit(SIMPLETEST_SCRIPT_EXIT_SUCCESS);
  }
  catch (Exception $e) {
    echo (string) $e;
    exit(SIMPLETEST_SCRIPT_EXIT_EXCEPTION);
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
