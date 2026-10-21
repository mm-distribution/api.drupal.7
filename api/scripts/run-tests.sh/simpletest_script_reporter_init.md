# simpletest_script_reporter_init()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 619–659 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L619-L659)

## Signature

```php
function simpletest_script_reporter_init()
```

## Documentation

```text
Initialize the reporter.
```

## Code

```php
function simpletest_script_reporter_init() {
  global $args, $all_tests, $test_list, $results_map;

  $results_map = array(
    'pass' => 'Pass',
    'fail' => 'Fail',
    'exception' => 'Exception'
  );

  echo "\n";
  echo "Drupal test run\n";
  echo "---------------\n";
  echo "\n";

  // Tell the user about what tests are to be run.
  if ($args['all']) {
    echo "All tests will run.\n\n";
  }
  else {
    echo "Tests to be run:\n";
    foreach ($test_list as $test_name) {
      if (strpos($test_name, '::') > 0) {
        list($test_class, $method) = explode('::', $test_name, 2);
        $info = call_user_func(array($test_class, 'getInfo'));
      } else {
        $info = call_user_func(array($test_name, 'getInfo'));
      }
      echo " - " . $info['name'] . ' (' . $test_name . ')' . "\n";
    }
    echo "\n";
  }

  echo "Test run started:\n";
  echo " " . format_date($_SERVER['REQUEST_TIME'], 'long') . "\n";
  timer_start('run-tests');
  echo "\n";

  echo "Test summary\n";
  echo "------------\n";
  echo "\n";
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
