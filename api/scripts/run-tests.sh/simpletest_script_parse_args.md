# simpletest_script_parse_args()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 213–281 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L213-L281)

## Signature

```php
function simpletest_script_parse_args()
```

## Documentation

```text
Parse execution argument and ensure that all are valid.

@return The list of arguments.
```

## Code

```php
function simpletest_script_parse_args() {
  // Set default values.
  $args = array(
    'script' => '',
    'help' => FALSE,
    'list' => FALSE,
    'clean' => FALSE,
    'url' => '',
    'php' => '',
    'concurrency' => 1,
    'all' => FALSE,
    'class' => FALSE,
    'file' => FALSE,
    'directory' => '',
    'color' => FALSE,
    'verbose' => FALSE,
    'cache' => FALSE,
    'cache-modules' => FALSE,
    'test_names' => array(),
    'fail-only' => FALSE,
    // Used internally.
    'test-id' => 0,
    'execute-test' => '',
    'xml' => '',
    'ci-parallel-node-index' => 1,
    'ci-parallel-node-total' => 1,
  );

  // Override with set values.
  $args['script'] = basename(array_shift($_SERVER['argv']));

  $count = 0;
  while ($arg = array_shift($_SERVER['argv'])) {
    if (preg_match('/--(\S+)/', $arg, $matches)) {
      // Argument found.
      if (array_key_exists($matches[1], $args)) {
        // Argument found in list.
        $previous_arg = $matches[1];
        if (is_bool($args[$previous_arg])) {
          $args[$matches[1]] = TRUE;
        }
        else {
          $args[$matches[1]] = array_shift($_SERVER['argv']);
        }
        // Clear extraneous values.
        $args['test_names'] = array();
        $count++;
      }
      else {
        // Argument not found in list.
        simpletest_script_print_error("Unknown argument '$arg'.");
        exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
      }
    }
    else {
      // Values found without an argument should be test names.
      $args['test_names'] += explode(',', $arg);
      $count++;
    }
  }

  // Validate the concurrency argument
  if (!is_numeric($args['concurrency']) || $args['concurrency'] <= 0) {
    simpletest_script_print_error("--concurrency must be a strictly positive integer.");
    exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
  }

  return array($args, $count);
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
